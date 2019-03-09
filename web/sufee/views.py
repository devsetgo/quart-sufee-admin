from quart import Quart
from quart import render_template
from quart import abort
from sufee import app

@app.route("/")
@app.route("/home")
async def index():
    template = 'index.html'
    return await render_template(template)

@app.route("/about")
async def aboutindex():
    template = 'about.html'
    return await render_template(template)

@app.route("/page-login")
async def login():
    template = "page-login.html"
    return await render_template(template)

@app.route("/page-register")
async def register():
    template = "page-register.html"
    return await render_template(template)

@app.route("/pages-forget")
async def page_forget():
    template = 'pages-forget.html'
    return await render_template(template)

@app.route("/ui-buttons")
async def ui_buttons():
    template = 'ui-buttons.html'
    return await render_template(template)

@app.route("/ui-badges")
async def ui_badges():
    template = 'ui-badges.html'
    return await render_template(template)


@app.route("/ui-tabs")
async def ui_tabs():
    template = 'ui-tabs.html'
    return await render_template(template)

@app.route("/charts-chartjs")
async def charts_chartjs():
    template = 'charts-chartjs.html'
    return await render_template(template)

@app.route("/charts-flot")
async def charts_flot():
    template = 'charts-flot.html'
    return await render_template(template)

@app.route("/charts-peity")
async def charts_peity():
    template = '/charts-peity.html'
    return await render_template(template)

@app.route("/font-fontawesome")
async def font_fontawesome():
    template = 'font-fontawesome.html'
    return await render_template(template)

@app.route("/font-themify")
async def font_themify():
    template = 'font-themify.html'
    return await render_template(template)

@app.route("/font-advanced")
async def font_advanced():
    template = 'font-advanced.html'
    return await render_template(template)

@app.route("/forms-basic")
async def forms_basic():
    template = 'forms-basic.html'
    return await render_template(template)

@app.route("/forms-advanced")
async def forms_advanced():
    template = 'forms-advanced.html'
    return await render_template(template)

@app.route("/frame")
async def frame():
    template = 'frame.html'
    return await render_template(template)

@app.route("/maps-gmap")
async def maps_gmap():
    template = 'maps-gmap.html'
    return await render_template(template)

@app.route("/maps-vector")
async def maps_vector():
    template = 'maps-vector.html'
    return await render_template(template)

@app.route("/tables-basic")
async def tables_basic():
    template = 'tables-basic.html'
    return await render_template(template)

@app.route("/tables-data")
async def tables_data():
    template = 'tables-data.html'
    return await render_template(template)

@app.route("/ui-alerts")
async def ui_alerts():
    template = 'ui-alerts.html'
    return await render_template(template)

@app.route("/ui-cards")
async def ui_cards():
    template = 'ui-cards.html'
    return await render_template(template)

@app.route("/ui-grids")
async def ui_grids():
    template = 'ui-grids.html'
    return await render_template(template)

@app.route("/ui-modals")
async def ui_modals():
    template = 'ui-modals.html'
    return await render_template(template)

@app.route("/ui-progressbar")
async def ui_progressbar():
    template = 'ui-progressbar.html'
    return await render_template(template)

@app.route("/ui-social-buttons")
async def ui_social_buttons():
    template = 'ui-social-buttons.html'
    return await render_template(template)

@app.route("/ui-switches")
async def ui_switches():
    template = 'ui-switches.html'
    return await render_template(template)

# @app.route("/ui-tabs")
# async def ui_tabs():
#     template = 'ui-tabs.html'
#     return await render_template(template)

@app.route("/ui-typography")
async def ui_typography():
    template = '/ui-typography.html'
    return await render_template(template)

@app.route("/widgets")
async def widgets():
    template = 'widgets.html'
    return await render_template(template)

