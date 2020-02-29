from flask import Flask, render_template
import tours_app.data as data

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def render_index():
    return render_template(
        "index.html",
        title=data.title,
        description=data.description,
        departures=data.departures,
        tours=data.tours,
    )


@app.route("/departure/<departure_code>/")
def render_departure(departure_code):
    tours = {
        tour_id: data.tours[tour_id]
        for tour_id in data.tours
        if data.tours[tour_id]["departure"] == departure_code
    }

    return render_template(
        "departure.html",
        departure_code=departure_code,
        departures=data.departures,
        tours=tours,
    )


@app.route("/tour/<tour_id>/")
def render_tour(tour_id):
    return render_template(
        "tour.html", tour=data.tours[int(tour_id)], departures=data.departures
    )
