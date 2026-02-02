@app.route("/stats")
def stats():
    counts = {}
    
    for student in students:
        meal = student["meal"]
        programme = student["programme"]
        
        counts[meal] = counts.get(meal, 0) +1
        counts[programme] = counts.get(programme, 0) +1
        
        return jsonify(counts)
    
    if__name__ == "__main__":
        app.run(debug=True)
        
        