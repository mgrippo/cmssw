/*! Contains useful functions to print histograms with ROOT.
This file is part of https://github.com/hh-italian-group/AnalysisTools. */

#pragma once

#include <TCanvas.h>
#include <TGraphAsymmErrors.h>
#include <TLegend.h>
#include <TPaveLabel.h>
#include <TRatioPlot.h>

#include "PlotPrimitives.h"

namespace root_ext {

class PlotRangeTuner {
public:
    using ValueType = double;
    using Hist = TH1;
    using Graph = TGraphAsymmErrors;

    static ValueType FindMinLimitX(const Hist& h, bool /*consired_errors*/);
    static ValueType FindMaxLimitX(const Hist& h, bool /*consired_errors*/);
    static ValueType FindMinLimitY(const Hist& h, bool consired_errors);
    static ValueType FindMaxLimitY(const Hist& h, bool consired_errors);
    static ValueType FindMinLimitX(const Graph& g, bool consired_errors);
    static ValueType FindMaxLimitX(const Graph& g, bool consired_errors);
    static ValueType FindMinLimitY(const Graph& g, bool consired_errors);
    static ValueType FindMaxLimitY(const Graph& g, bool consired_errors);

    template<typename Item>
    void Add(const Item& item, bool scan_x, bool consider_errors)
    {
        if(scan_x) {
            x_min = std::min(x_min, PlotRangeTuner::FindMinLimitX(item, consider_errors));
            x_max = std::max(x_max, PlotRangeTuner::FindMaxLimitX(item, consider_errors));
        } else {
            UpdateLimitsX(item);
        }

        y_min = std::min(y_min, PlotRangeTuner::FindMinLimitY(item, consider_errors));
        y_max = std::max(y_max, PlotRangeTuner::FindMaxLimitY(item, consider_errors));
    }

    ValueType GetYMinValue(bool log_y, ValueType min_y_sf, ValueType y_min_log) const;
    ValueType GetYMaxValue(ValueType max_y_sf, ValueType y_min_value) const;
    ValueType GetXMinValue() const;
    ValueType GetXMaxValue() const;
    TH1F* DrawFrame(TPad& pad, bool log_y, ValueType max_y_sf, ValueType min_y_sf, ValueType y_min_log) const;
    void SetRangeX(TAxis& x_axis) const;
    void SetRangeY(TAxis& y_axis, bool log_y, ValueType max_y_sf, ValueType min_y_sf, ValueType y_min_log) const;

    template<typename Item>
    void SetItemRangeY(Item& ref_item, bool log_y, ValueType max_y_sf, ValueType min_y_sf, ValueType y_min_log) const
    {
        const ValueType y_min_value = GetYMinValue(log_y, min_y_sf, y_min_log);
        ref_item.SetMinimum(y_min_value);
        ref_item.SetMaximum(GetYMaxValue(max_y_sf, y_min_value));
    }

private:
    void UpdateLimitsX(const Hist& h);
    void UpdateLimitsX(const Graph& g);

public:
    ValueType x_min{std::numeric_limits<ValueType>::max()};
    ValueType x_max{std::numeric_limits<ValueType>::lowest()};
    ValueType y_min{std::numeric_limits<ValueType>::max()};
    ValueType y_max{std::numeric_limits<ValueType>::lowest()};
};

namespace plotting {
template<typename T>
std::shared_ptr<TPaveLabel> NewPaveLabel(const Box<T>& box, const std::string& text)
{
    return std::make_shared<TPaveLabel>(box.left_bottom().x(), box.left_bottom().y(),
                                        box.right_top().x(), box.right_top().y(), text.c_str());
}

template<typename T>
std::shared_ptr<TPad> NewPad(const Box<T>& box)
{
    static const char* pad_name = "pad";
    return std::make_shared<TPad>(pad_name, pad_name, box.left_bottom().x(), box.left_bottom().y(),
                                  box.right_top().x(), box.right_top().y());
}

template<typename T>
std::shared_ptr<TCanvas> NewCanvas(const Size<T, 2>& size)
{
    static const char* canvas_name = "canvas";
    return std::make_shared<TCanvas>(canvas_name, canvas_name, size.x(), size.y());
}

template<typename T>
void SetMargins(TPad& pad, const MarginBox<T>& box, TPad* ratio_pad = nullptr, float ratio_pad_y_size_sf = 1.f,
                float main_ratio_margin = .02f)
{
    pad.SetLeftMargin(box.left());
    pad.SetRightMargin(box.right());
    pad.SetTopMargin(box.top());

    if(ratio_pad) {
        ratio_pad->SetLeftMargin(box.left());
        ratio_pad->SetRightMargin(box.right());
        ratio_pad->SetBottomMargin(box.bottom() * ratio_pad_y_size_sf);
        ratio_pad->SetTopMargin(main_ratio_margin / 2 * ratio_pad_y_size_sf);
        pad.SetBottomMargin(main_ratio_margin / 2);
    } else {
        pad.SetBottomMargin(box.bottom());
    }
}

template<typename T>
void SetMargins(TRatioPlot& plot, const MarginBox<T>& box)
{
    plot.SetLeftMargin(box.left());
    plot.SetLowBottomMargin(box.bottom());
    plot.SetRightMargin(box.right());
    plot.SetUpTopMargin(box.top());
}

template<typename Range = ::analysis::Range<double>>
std::shared_ptr<TGraphAsymmErrors> HistogramToGraph(const TH1& hist, bool divide_by_bin_width = false,
                                                    const ::analysis::MultiRange<Range>& blind_ranges = {})
{
    std::vector<double> x, y, exl, exh, eyl, eyh;
    size_t n = 0;
    for(int bin = 1; bin <= hist.GetNbinsX(); ++bin) {
        const Range bin_range(hist.GetBinLowEdge(bin), hist.GetBinLowEdge(bin + 1),
                              ::analysis::RangeBoundaries::MinIncluded);
        if(blind_ranges.Overlaps(bin_range))
            continue;
        x.push_back(hist.GetBinCenter(bin));
        exl.push_back(x[n] - hist.GetBinLowEdge(bin));
        exh.push_back(hist.GetBinLowEdge(bin + 1) - x[n]);
        y.push_back(hist.GetBinContent(bin));
        eyl.push_back(hist.GetBinErrorLow(bin));
        eyh.push_back(hist.GetBinErrorUp(bin));
        if(divide_by_bin_width) {
            const double bin_width = hist.GetBinWidth(bin);
            y[n] /= bin_width;
            eyl[n] /= bin_width;
            eyh[n] /= bin_width;
        }
        ++n;
    }
    return std::make_shared<TGraphAsymmErrors>(static_cast<int>(n), x.data(), y.data(), exl.data(), exh.data(),
                                               eyl.data(), eyh.data());
}

template<typename Hist>
std::shared_ptr<TGraphAsymmErrors> CreateRatioGraph(const TGraphAsymmErrors& graph, const Hist& hist)
{
    auto ratio_graph = std::make_shared<TGraphAsymmErrors>(graph);
    for(int i = 0, k = 0; i < graph.GetN(); ++i) {
        const double x = graph.GetX()[i];
        const double y = graph.GetY()[i];
        const double ey_low = graph.GetEYlow()[i];
        const double ey_high = graph.GetEYhigh()[i];
        const int bin = hist.FindFixBin(x);
        const double hist_y = hist.GetBinContent(bin);
        if(hist_y != 0) {
            ratio_graph->GetY()[k] = y / hist_y;
            ratio_graph->GetEYlow()[k] = ey_low / hist_y;
            ratio_graph->GetEYhigh()[k] = ey_high / hist_y;
            ++k;
        } else {
            ratio_graph->RemovePoint(k);
        }
    }
    return ratio_graph;
}

template<typename Hist>
std::shared_ptr<Hist> CreateNormalizedUncertaintyHistogram(const Hist& hist)
{
    auto norm_hist = std::make_shared<Hist>(hist);
    for(int i = 1; i <= hist.GetNbinsX(); ++i) {
        const double y = hist.GetBinContent(i);
        const double ey = hist.GetBinError(i);
        norm_hist->SetBinContent(i, 1.);
        if(ey == 0 && y == 0)
            norm_hist->SetBinError(i, 0);
        else
            norm_hist->SetBinError(i, ey / y);
    }
    return norm_hist;
}

void DivideByBinWidth(TH1& histogram);
void ApplyAdditionalUncertainty(TH1& histogram, double unc);

} // namespace plotting
} // root_ext
