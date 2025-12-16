import matplotlib.pyplot as plt
from analyzer import DataAnalyzer


# Decorator for dashboard header (automation feature)
def dashboard_header(func):
    def wrapper(*args, **kwargs):
        print("\n====== COVID-19 DASHBOARD ======")
        return func(*args, **kwargs)
    return wrapper


# Report class for summaries
class Report:
    def __init__(self, analyzer: DataAnalyzer):
        self.analyzer = analyzer

    def print_summary(self):
        avg_recovery = self.analyzer.average_recovery_rate()
        avg_mortality = self.analyzer.average_mortality_rate()
        avg_growth = self.analyzer.average_growth_rate()

        print("\n----- Summary Report -----")
        print(f"Average Recovery Rate: {avg_recovery:.2f}%")
        print(f"Average Mortality Rate: {avg_mortality:.2f}%")
        print(f"Average Growth Rate: {avg_growth:.2f}%")
        print("--------------------------")


@dashboard_header
def run_dashboard():
    analyzer = DataAnalyzer('csv_data.csv')
    analyzer.load_data()

    cities = analyzer.cities

    names = [c.name for c in cities]
    confirmed = [c.confirmed for c in cities]
    recovered = [c.recovered for c in cities]
    active = [c.active for c in cities]
    growth_rates = [c.growth_rate() for c in cities]

    # lambda for percentage formatting (requirement)
    fmt_percent = lambda x: f"{x:.2f}%"  # noqa: E731

    for city in cities:
        print(city)
        print(f"Recovery Rate: {fmt_percent(city.recovery_rate())}")
        print(f"Mortality Rate: {fmt_percent(city.mortality_rate())}")
        print(f"Growth Rate:   {fmt_percent(city.growth_rate())}")
        print(f"Severity: {city.severity_level()}\n")

    # Visualization: stacked bars + trend line
    x = range(len(names))
    plt.figure()

    # multi-bar stacked comparison
    plt.bar(x, confirmed, label='Confirmed', color='#1f77b4')
    plt.bar(x, recovered, bottom=confirmed, label='Recovered', color='#ff7f0e')
    bottom_for_active = [c + r for c, r in zip(confirmed, recovered)]
    plt.bar(x, active, bottom=bottom_for_active, label='Active', color='#2ca02c')

    # trend line (growth rate) on second y-axis
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax2.plot(x, growth_rates, color='red', marker='o', label='Growth Rate (%)')

    ax1.set_xticks(list(x))
    ax1.set_xticklabels(names)
    ax1.set_title('COVID-19 City Comparison')
    ax1.set_ylabel('Cases')
    ax2.set_ylabel('Growth Rate (%)')

    # combined legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper right')

    plt.tight_layout()
    plt.show()

    print("Critical Cities:", analyzer.critical_cities())

    # summary report
    report = Report(analyzer)
    report.print_summary()


if __name__ == '__main__':
    run_dashboard()
