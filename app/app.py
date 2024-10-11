from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON

from dummy_service import DashboardDummyDataService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class DashboardConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dashboard_config = db.Column(JSON)


@app.route('/dashboard_config', methods=['GET', 'POST'])
def handle_dashboard_config():
    if request.method == 'POST':
        data = request.json
        config = DashboardConfig(dashboard_config=data)
        db.session.add(config)
        db.session.commit()
        return jsonify({"message": "Dashboard config saved successfully", "id": config.id}), 201
    
    elif request.method == 'GET':
        config = DashboardConfig.query.order_by(DashboardConfig.id.desc()).first()
        if config:
            return jsonify(config.dashboard_config)
        else:
            return jsonify({"message": "No dashboard config found"}), 404

@app.route('/avg_dwell_time', methods=['GET'])
def get_avg_dwell_time():
    return jsonify({"avg_dwell_time": DashboardDummyDataService.dummy_get_avg_dwell_time_for_site()})

@app.route('/total_guests', methods=['GET'])
def get_total_guests():
    return jsonify({"total_guests": DashboardDummyDataService.dummy_get_total_num_guests()})

@app.route('/new_guests', methods=['GET'])
def get_new_guests():
    return jsonify({"new_guests": DashboardDummyDataService.dummy_get_total_new_guests()})

@app.route('/online_guests', methods=['GET'])
def get_online_guests():
    return jsonify({"online_guests": DashboardDummyDataService.dummy_get_currently_online_guests()})

@app.route('/bounce_rate', methods=['GET'])
def get_bounce_rate():
    return jsonify({"bounce_rate": DashboardDummyDataService.dummy_get_site_bounce_rate()})

@app.route('/login_graph', methods=['GET'])
def get_login_graph():
    return jsonify(DashboardDummyDataService.dummy_get_site_login_graph())

@app.route('/activity_graph', methods=['GET'])
def get_activity_graph():
    return jsonify(DashboardDummyDataService.dummy_get_site_activity_graph())

@app.route('/latest_guests', methods=['GET'])
def get_latest_guests():
    siteid = request.args.get('siteid', 1)
    guests = DashboardDummyDataService.dummy_get_site_latest_guests(siteid=siteid)
    return jsonify([{
        "firstname": g.firstname,
        "email": g.email,
        "dob": str(g.dob),
        "phonenumber": g.phonenumber,
        "gender": g.gender,
        "first_seen": g.first_seen.isoformat(),
        "last_seen_at": g.last_seen_at.isoformat()
    } for g in guests])

@app.route('/gender_segments', methods=['GET'])
def get_gender_segments():
    return jsonify(DashboardDummyDataService.dummy_get_site_gender_segments())

@app.route('/visits_segment', methods=['GET'])
def get_visits_segment():
    return jsonify(DashboardDummyDataService.dummy_get_site_visits_segment())

@app.route('/successful_payments', methods=['GET'])
def get_successful_payments():
    return jsonify({"successful_payments": DashboardDummyDataService.dummy_get_successful_payments()})

@app.route('/recurring_payments', methods=['GET'])
def get_recurring_payments():
    return jsonify({"recurring_payments": DashboardDummyDataService.dummy_get_recurring_payments()})

@app.route('/daily_transactions', methods=['GET'])
def get_daily_transactions():
    return jsonify(DashboardDummyDataService.dummy_get_daily_transactions())

@app.route('/once_guests', methods=['GET'])
def get_once_guests():
    return jsonify({"once_guests": DashboardDummyDataService.dummy_get_only_once_guests()})

@app.route('/last_transactions', methods=['GET'])
def get_last_transactions():
    count = request.args.get('count', 5, type=int)
    return jsonify(DashboardDummyDataService.dummy_get_last_n_transactions(count=count))

@app.route('/most_transactions_package', methods=['GET'])
def get_most_transactions_package():
    return jsonify(DashboardDummyDataService.dummy_get_most_transactions_package())

@app.route('/active_vouchers', methods=['GET'])
def get_active_vouchers():
    return jsonify(DashboardDummyDataService.dummy_get_active_vouchers())

@app.route('/unused_vouchers', methods=['GET'])
def get_unused_vouchers():
    return jsonify(DashboardDummyDataService.dummy_get_unused_vouchers())

@app.route('/vouchers_near_expiry', methods=['GET'])
def get_vouchers_near_expiry():
    return jsonify(DashboardDummyDataService.dummy_get_vouchers_near_expiry())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0',port=5000)
