/*! Print event selection histograms.
This file is part of https://github.com/hh-italian-group/AnalysisTools. */

#include <iostream>

#include "AnalysisTools/Run/include/program_main.h"
#include "AnalysisTools/Core/include/RootExt.h"
#include "../include/RootPrintToPdf.h"

struct Arguments {
    REQ_ARG(std::string, outputFileName);
    REQ_ARG(std::vector<std::string>, args);
};

class Print_Selection {
public:
    using FileTagPair = std::pair<std::string, std::string>;
    using Printer = root_ext::PdfPrinter;
    using MyHistogramSource = root_ext::SimpleHistogramSource<TH1D, Double_t>;

    Print_Selection(const Arguments& arguments):
       printer(arguments.outputFileName())
    {
        for(const std::string& inputName : arguments.args()) {
            const size_t split_index = inputName.find_first_of(':');
            const std::string fileName = inputName.substr(0, split_index);
            const std::string tagName = inputName.substr(split_index + 1);
            inputs.push_back(FileTagPair(fileName, tagName));
        }
        for(const FileTagPair& fileTag : inputs) {
            auto file = root_ext::OpenRootFile(fileTag.first);
            source.Add(fileTag.second, file);
        }
    }

    void Run()
    {
        page.side.use_log_scaleY = true;
        page.side.layout.has_legend = false;

        PrintAll("Selection_event", "Event selection");
        PrintAll("Selection_muons", "Muon selection");
        PrintAll("Selection_taus", "Tau selection");
        PrintAll("Selection_electrons_bkg", "Bkg Electron selection");
        PrintAll("Selection_bjets", "b-jet selection");
    }

private:
    void PrintAll(const std::string& name, const std::string& title, std::string second_suffix = "")
    {
        try {
            Print(name, title, AddSuffix("", second_suffix), "Number of entries");
            Print(name, title, AddSuffix("effRel", second_suffix), "Relative efficiency");
            Print(name, title, AddSuffix("effAbs", second_suffix), "Absolute efficiency");
        } catch(std::runtime_error& e) {
            std::cerr << "ERROR: " << e.what() << std::endl;
        }
    }

    void Print(const std::string& name, const std::string& title,
               std::string name_suffix = "", std::string title_suffix = "")
    {
        page.side.histogram_name = AddSuffix(name, name_suffix);
        page.title = page.side.histogram_title = AddSuffix(title, title_suffix, ". ");
        printer.Print(page, source);
    }

    static std::string AddSuffix(const std::string& name, const std::string& suffix, std::string separator = "_")
    {
        std::ostringstream full_name;
        full_name << name;
        if(suffix.size())
            full_name << separator << suffix;
        return full_name.str();
    }

private:
    std::vector<FileTagPair> inputs;
    MyHistogramSource source;
    root_ext::SingleSidedPage page;
    Printer printer;
};

PROGRAM_MAIN(Print_Selection, Arguments)
