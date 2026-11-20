from shiny import ui, render, App
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


# UI ----------------

# Datasets
# -------
data = pd.read_csv('Data/borough_demographics.csv')

# Defining data with and without the City of London uncluded
with_cl = data.copy()
with_cl['group'] = 'Including the City'

without_cl = data.copy().drop(index=31)
without_cl['group'] = 'Not including the City'

both = pd.concat([with_cl, without_cl], ignore_index=True)
# -------

# Options for sidebar
# -------
options = {
    'with': 'Including the City',
    'without': 'Not including the City',
    'both': 'Comparison of Both'
}

datasets = {
    'with': with_cl,
    'without': without_cl,
    'both': both
}
# -------

# UI
# -------
app_ui = ui.page_fluid(
    ui.card(
        ui.card_header('The Graph!'),
        ui.output_plot('plot')
    ),
    ui.card(

        ui.card_header('Choose Dataset'),
        ui.input_select('dataset', 'Dataset', choices=options, selected="both"),
        #title='Choose Dataset',
    ),
    ui.card(
        ui.card_header('Regression Analysis!'),
        ui.output_ui('regression'),


))
# -------

# Plot function
# -------
def make_plot(data_set, label):

    # Making the Plot
    plot = sns.pairplot(data=data_set,
                kind='reg',
                y_vars = ['health_score', 'wealth_score'],
                x_vars = ['green_area_hectare', 'blue _area_hectare', 'green+blue_area_hectare',
                        'percent_green', 'percent_blue', 'percent_green+blue'],
                hue = 'group',
                hue_order=[
                    'Including the City', 'Not including the City'
                ],
                palette = {
                    'Including the City': '#009E73',
                    'Not including the City': '#CC79A7'
                },
                markers=[
                    '+', 'x'
                ],
                plot_kws={'scatter_kws': {'s': 15, 'linewidths': 1},
                        'line_kws': {'lw': 1},              
                    
                })

    # Editing titles, axis, legends etc. for legibility
    

    plot._legend.remove()

    if label == 'Comparison of Both':
        plot.add_legend(markerscale=3, title='', loc='upper right', bbox_to_anchor=(1,1))


    plot.figure.text(0.02,0.9, f'using the "{label}" dataset', ha='left', fontsize=12)
    plot.figure.subplots_adjust(top=0.86)
    plot.figure.suptitle('Plot of Health and Wealth against blue and green spaces in London Boroughs', x=0.02, y=0.98, ha='left')
    plot.figure.set_size_inches(10,7)
    plot.figure.subplots_adjust(wspace=0.1, hspace=0.1)
    plot.figure.subplots_adjust(left=0.08, right=1.5, bottom=0.2, top=0.89)
    

    #plt.tight_layout()



    return plot

def reg(data_set):

    formula_string = "Q('health_score') ~ Q('percent_green') + Q('wealth_score')"

    model_full = sm.formula.ols(formula = formula_string, data = data_set)
    model_full_fitted = model_full.fit()

    return model_full_fitted.summary()
# -------


# Server ----------------

def server(input, output, session):
    @render.plot
    def plot():
        choice = input.dataset()
        return make_plot(datasets[choice], options[choice])
    
    @render.ui
    def regression():
        choice = input.dataset()
        return ui.div(
            ui.tags.style("""
            .simpletable { border-collapse: collapse; margin: 1rem 0; }
            .simpletable th, .simpletable td { border: 1px solid #ccc; padding: 6px 10px; }
            """),
        ui.HTML(reg(datasets[choice]).as_html())
        )
# APP ----------------

app = App(app_ui, server)
