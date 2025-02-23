import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import json, datetime, os, pprint
import seaborn as sns
import numpy as np


subjects = {
    "PHYSICS": {
        "Mechanics": [
            "Units and Measurements (PUC-I)",
            "Motion in a Straight Line (PUC-I)",
            "Motion in a Plane (PUC-I)",
            "Laws of Motion (PUC-I)",
            "Work, Energy and Power (PUC-I)",
            "System of Particles and Rotational Motion (PUC-I)",
            "Gravitation (PUC-I)",
            "Mechanical Properties of Solids (PUC-I)",
            "Mechanical Properties of Fluids (PUC-I)"
        ],
        "Thermodynamics and Kinetic Theory": [
            "Thermal Properties of Matter (PUC-I)",
            "Thermodynamics (PUC-I)",
            "Kinetic Theory (PUC-I)"
        ],
        "Waves and Oscillations": [
            "Oscillations (PUC-I)",
            "Waves (PUC-I)"
        ],
        "Electricity and Magnetism": [
            "Electric Charges and Fields (PUC-II)",
            "Electrostatic Potential and Capacitance (PUC-II)",
            "Current Electricity (PUC-II)",
            "Moving Charges and Magnetism (PUC-II)",
            "Magnetism and Matter (PUC-II)",
            "Electromagnetic Induction (PUC-II)",
            "Alternating Current (PUC-II)"
        ],
        "Optics": [
            "Electromagnetic Waves (PUC-II)",
            "Ray Optics and Optical Instruments (PUC-II)",
            "Wave Optics (PUC-II)"
        ],
        "Modern Physics": [
            "Dual Nature of Radiation and Matter (PUC-II)",
            "Atoms (PUC-II)",
            "Nuclei (PUC-II)",
            "Semiconductor Electronics Materials, Devices and Simple Circuits (PUC-II)"
        ]
    },
    "CHEMISTRY": {
        "Physical Chemistry": [
            "Some Basic Concepts of Chemistry (PUC-I)",
            "Structure of Atom (PUC-I)",
            "Classification of Elements and Periodicity in Properties (PUC-I)",
            "Chemical Bonding and Molecular Structure (PUC-I)",
            "Thermodynamics (PUC-I)",
            "Equilibrium (PUC-I)",
            "Redox Reactions (PUC-I)",
            "Solutions (PUC-II)",
            "Electrochemistry (PUC-II)",
            "Chemical Kinetics (PUC-II)"
        ],
        "Inorganic Chemistry": [
            "The d and f Block Elements (PUC-II)",
            "Coordination Compounds (PUC-II)"
        ],
        "Organic Chemistry": [
            "Organic Chemistry: Some Basic Principles and Techniques (PUC-I)",
            "Hydrocarbons (PUC-I)",
            "Haloalkanes and Haloarenes (PUC-II)",
            "Alcohols, Phenols and Ethers (PUC-II)",
            "Aldehydes, Ketones and Carboxylic Acids (PUC-II)",
            "Amines (PUC-II)",
            "Biomolecules (PUC-II)"
        ]
    },
    "MATHEMATICS": {
        "Algebra": [
            "Sets (PUC-I)",
            "Relations and Functions (PUC-I)",
            "Complex Numbers and Quadratic Equations (PUC-I)",
            "Linear Inequalities (PUC-I)",
            "Permutations and Combinations (PUC-I)",
            "Binomial Theorem (PUC-I)",
            "Sequences and Series (PUC-I)",
            "Matrices (PUC-II)",
            "Determinants (PUC-II)"
        ],
        "Trigonometry": [
            "Trigonometric Functions (PUC-I)",
            "Inverse Trigonometric Functions (PUC-II)"
        ],
        "Coordinate Geometry": [
            "Straight Lines (PUC-I)",
            "Conic Sections (PUC-I)",
            "Introduction to Three Dimensional Geometry (PUC-I)",
            "Three Dimensional Geometry (PUC-II)"
        ],
        "Calculus": [
            "Limits and Derivatives (PUC-I)",
            "Continuity and Differentiability (PUC-II)",
            "Application of Derivatives (PUC-II)",
            "Integrals (PUC-II)",
            "Application of Integrals (PUC-II)",
            "Differential Equations (PUC-II)"
        ],
        "Statistics and Probability": [
            "Statistics (PUC-I)",
            "Probability (PUC-I)",
            "Probability (PUC-II)"
        ],
        "Linear Programming": [
            "Linear Programming (PUC-II)"
        ],
        "Vector Algebra": [
            "Vector Algebra (PUC-II)"
        ]
    }
}

# subject = input("MATHEMATICS, PHYSICS, CHEMISTRY: ")
# roll_number = int(input("Roll No: "))
# date = input("Enter Date (DD/MM//YY): ")
# subject = "PHYSICS"
# roll_number = 242007
# data_processed_path = f"Data/Processed/{subject}/{roll_number}.json"
# common_data_processed_path = f"Data/Processed/{subject}/common_data.json"

os.makedirs("Data/Graph", exist_ok=True)
def get_data(data_processed_path, common_data_processed_path):

    with open(data_processed_path, 'r') as data_file:
        student_data = json.load(data_file)

    with open(common_data_processed_path) as common_data_file:
        common_data = json.load(common_data_file)
    
    return student_data, common_data


def student_class_avg_datewise(student_data, common_data):
    dates = []
    student_avg = []
    class_avg = []
    for tests in student_data:
        for test in tests:
            dates.append(test.split("-")[0])
            student_avg.append(tests[test]['Avg_of_test'])
    for tests in common_data:
        for test in tests:
            if test.split("-")[0] in dates:
                class_avg.append(tests[test]['Avg_of_class'])
    dates = [datetime.datetime.strptime(d, "%d/%m/%Y") for d in dates]
    print(dates)
    plt.figure(figsize=(8, 5))

    plt.xlim(min(dates), max(dates))
    plt.ylim(min(class_avg)-5, max(student_avg)+10)
    
    plt.plot(dates, student_avg, label="Student Average", color="blue", linewidth=2, marker="o", markersize=6)
    plt.plot(dates, class_avg, label="Class Average", color="gray", linewidth=2, linestyle="dashed", marker="s", markersize=6)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.xticks(dates, [d.strftime('%d/%m') for d in dates], fontsize=8, rotation=45) 

    plt.xlabel("Test Date", fontsize=12)
    plt.ylabel("Score", fontsize=12)
    plt.title("Student Performance vs Class Average", fontsize=14, fontweight="bold")   

    plt.legend(loc="upper left", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    # plt.savefig(f"Data/Graph/{roll_number}_DATE_AVG.png")
    plt.show()

def generate_grayscale_heatmaps(student_data, common_data):
    test_dates = []
    student_scores = {}
    class_scores = {}
    
    for test in student_data:
        for test_id, test_info in test.items():
            date = test_id.split("-")[0]
            if date not in test_dates:
                test_dates.append(date)
            for chapter, score in test_info["Avg_of_student_chapter_wise"].items():
                if chapter not in student_scores:
                    student_scores[chapter] = []
                student_scores[chapter].append(score)
    
    for test in common_data:
        for test_id, test_info in test.items():
            date = test_id.split("-")[0]
            for chapter, score in test_info["Avg_of_class_chapter_wise"].items():
                if chapter not in class_scores:
                    class_scores[chapter] = []
                class_scores[chapter].append(score)
    
    student_df = pd.DataFrame.from_dict(student_scores, orient='index', columns=test_dates).fillna(0)
    class_df = pd.DataFrame.from_dict(class_scores, orient='index', columns=test_dates).fillna(0)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 8), sharey=True, gridspec_kw={'width_ratios': [1, 1.2]})  
    
    sns.heatmap(student_df, cmap="gray_r", annot=True, fmt=".0f", yticklabels=False, cbar=False, 
                linewidths=0.5, linecolor='black', vmin=0, vmax=100, ax=axes[0])
    axes[0].set_title("Student Performance Heatmap")
    axes[0].set_xlabel("Test Date")
    axes[0].set_ylabel("")
    
    sns.heatmap(class_df, cmap="gray_r", annot=True, fmt=".0f", yticklabels=True, linecolor='black', 
                linewidths=0.5, vmin=0, vmax=100, ax=axes[1])
    axes[1].set_title("Class Average Performance Heatmap")
    axes[1].set_xlabel("Test Date")
    axes[1].set_ylabel("")

    axes[1].yaxis.set_label_position("left")
    axes[1].yaxis.tick_left()

    plt.subplots_adjust(wspace=0.05)  

    plt.tight_layout()
    plt.savefig("Data/Graph/student_vs_class_heatmaps.png", dpi=300, bbox_inches='tight')
    plt.show()

def group_by_topics(data, subject, who):
    grouped_data = {}
    
    for test_data in data:
        test = list(test_data.keys())[0]
        temp = test_data[test][f'Avg_of_{who}_chapter_wise']
        
        if test not in grouped_data:
            grouped_data[test] = {}

        for topic, chapters in subjects[subject].items():
            if topic not in grouped_data[test]:
                grouped_data[test][topic] = 0 
                count = 0  

            for chapter_main in chapters:
                if chapter_main in temp:
                    grouped_data[test][topic] += temp[chapter_main]
                    count += 1

            if count > 0:
                grouped_data[test][topic] = round(grouped_data[test][topic] / count, 2)
    
    return grouped_data





# def plot_topicwise_trends(data):
#     grouped_data = group_by_topics(data)
#     plt.figure(figsize=(10, 6))
    
#     all_scores = []
#     for topic in next(iter(grouped_data.values())):
#         dates = list(grouped_data.keys())
#         scores = [grouped_data[date][topic] for date in dates]
#         dates = list(map(lambda x:  x.split('-')[0], list(grouped_data.keys())))
#         all_scores.extend(scores)
#         plt.plot(dates, scores, marker='o', label=topic)

#     if all_scores:
#         plt.ylim(min(all_scores)-5, max(all_scores)+10)
    
#     plt.xlabel("Test Date")
#     plt.ylabel("Average Score")
#     plt.title("Topic-wise Performance Trend")

#     plt.xticks(fontsize=8)

#     plt.legend()
#     plt.grid(True, linestyle="--", alpha=0.6)
#     plt.tight_layout()
#     plt.show()

# plot_topicwise_trends(student_data)


if __name__ == "__main__":
    print("ALLO!")
    topic = []
    for topics in subjects["CHEMISTRY"]:
        topic.append(topics)
    print(topic)