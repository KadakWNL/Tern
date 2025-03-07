import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import json, datetime, os, pprint
import seaborn as sns
import numpy as np
import plotly.graph_objects as go
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
date = r"05/01/2025"
subject = "PHYSICS"
roll_number = 242007
data_processed_path = rf"Data/Processed/{subject}/{roll_number}.json"
common_data_processed_path = rf"Data/Processed/{subject}/common_data.json"

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
    # print(dates)


def student_class_avg_datewise(student_data, common_data):
    sns.set_style("whitegrid")  # Clean look with grid

    # Extract data
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

    # Convert dates to datetime format
    dates = [datetime.datetime.strptime(d, "%d/%m/%Y") for d in dates]

    # Create a DataFrame for Seaborn
    df = pd.DataFrame({
        "Date": dates,
        "Student Average": student_avg,
        "Class Average": class_avg
    })

    # Melt the DataFrame for Seaborn
    df_melted = df.melt(id_vars=["Date"], var_name="Type", value_name="Score")

    # Create the plot
    plt.figure(figsize=(6, 6))  
    ax = sns.lineplot(data=df_melted, x="Date", y="Score", hue="Type", style="Type",
                      markers=True,  
                      dashes=False,  
                      errorbar=None,  
                      palette={"Student Average": "royalblue", "Class Average": "gray"},
                      linewidth=2, markersize=8)

    # **Set X-axis grid every 5 days**
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))  # X-grid every 5 days
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))  # Format dates

    # Rotate X-ticks for readability
    plt.xticks(fontsize=9, rotation=45)

    # Labels and Title
    ax.set_xlabel("Test Date", fontsize=12)
    ax.set_ylabel("Score", fontsize=12)
    ax.set_title("Student Performance vs Class Average", fontsize=14, fontweight="bold")

    # **Keep X and Y axes visible**
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(True)
    ax.spines["bottom"].set_visible(True)

    # **Enable grid with X-grid every 5 days**
    ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.6)

    # Adjust legend
    legend = ax.legend(title="Type", loc="upper right", fontsize=10)
    legend.get_frame().set_linewidth(0)
    legend.get_frame().set_facecolor('none')

    plt.tight_layout()
    plt.savefig("Data/Graph/student_performance_over_time.png", dpi=300, bbox_inches='tight')
    plt.show()


def generate_grayscale_heatmaps(student_data, common_data,subject=None):
    test_dates = []
    student_scores = {}
    class_scores = {}
    subject="PHYSICS"
    student_data, class_data = group_by_topics(student_data,subject,"student"),group_by_topics(common_data,subject,"class")
    for test in student_data:
        date=test.split("-")[0]
        if date not in test_dates:
            test_dates.append(date)
        for block_of_chapter,score in student_data[test].items():
            if block_of_chapter not in student_scores:
                student_scores[block_of_chapter]=[]
            student_scores[block_of_chapter].append(score)                

    for test in class_data:
        date=test.split("-")[0]
        if date not in test_dates:
            test_dates.append(date)
        for block_of_chapter,score in class_data[test].items():
            if block_of_chapter not in class_scores:
                class_scores[block_of_chapter]=[]
            class_scores[block_of_chapter].append(score)             
    # for test in student_data:
    #     for test_id, test_info in test.items():
    #         date = test_id.split("-")[0]
    #         if date not in test_dates:
    #             test_dates.append(date)
    #         for chapter, score in test_info["Avg_of_student_chapter_wise"].items():
    #             if chapter not in student_scores:
    #                 student_scores[chapter] = []
    #             student_scores[chapter].append(score)
    # print(student_scores)
    
    # for test in common_data:
    #     for test_id, test_info in test.items():
    #         date = test_id.split("-")[0]
    #         for chapter, score in test_info["Avg_of_class_chapter_wise"].items():
    #             if chapter not in class_scores:
    #                 class_scores[chapter] = []
    #             class_scores[chapter].append(score)
    # print(class_scores)
    student_df = pd.DataFrame.from_dict(student_scores, orient='index', columns=test_dates).fillna(0)
    class_df = pd.DataFrame.from_dict(class_scores, orient='index', columns=test_dates).fillna(0)
    
    fig, axes = plt.subplots(1, 2, figsize=(7.75, 4.5), sharey=True, gridspec_kw={'width_ratios': [1, 1.2]})  
    
    sns.heatmap(student_df, cmap="RdYlGn", annot=True, fmt=".0f", yticklabels=False, cbar=False, 
                linewidths=0.3, linecolor='black', vmin=0, vmax=100, ax=axes[0])
    axes[0].set_title(f"Performance of {roll_number}")
    axes[0].set_xlabel("Test Date")
    axes[0].set_ylabel("")
    
    sns.heatmap(class_df, cmap="RdYlGn", annot=True, fmt=".0f", yticklabels=True, linecolor='black', 
                linewidths=0.3, vmin=0, vmax=100, ax=axes[1])
    axes[1].set_title("Class Avg Performance")
    axes[1].set_xlabel("Test Date")
    axes[1].set_ylabel("")

    axes[1].yaxis.set_label_position("left")
    axes[1].yaxis.tick_left()

    plt.subplots_adjust(wspace=1.25)  
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
    # print(grouped_data)
    return grouped_data



def plot_student_vs_class_avg_spi(student_data,class_data):
    for value in student_data[-1]:
        student_spi=student_data[-1][value]["Avg_SPI_till_date"]
    for value in class_data[-1]:
        class_spi=class_data[-1][value]["Avg_SPI_of_class_till_date"]
    categories = ["Class SPI", "Student SPI"]
    values = [class_spi, student_spi]

    # Create horizontal bar plot
    plt.figure(figsize=(8, 1.2))
    bars = plt.barh(categories, values, color=['red', 'green'], height=0.3)
    for bar, value in zip(bars, values):
        plt.text(value + 2, bar.get_y() + bar.get_height()/2, str(value), va='center', fontsize=12, fontweight='bold')

    # Labels and title
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.xlabel("SPI Score")
    plt.title("Class SPI vs Student SPI Comparison")
    plt.xlim(0, 100)  # Assuming SPI is out of 100
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.gcf().set_size_inches(8, 2)
    plt.savefig("Data/Graph/student_vs_class_spi.png", dpi=300, bbox_inches='tight')
    plt.show()




# def create_pie_chart_for_distribution_comparison(student_data,class_data):
#     grouped_data = {}
#     test_data=student_data[-1]
#     test = list(test_data.keys())[0]
#     temp = test_data[test][f'Avg_of_student_chapter_wise']
    
#     if test not in grouped_data:
#         grouped_data[test] = {}

#     for topic, chapters in subjects[subject].items():
#         if topic not in grouped_data[test]:
#             grouped_data[test][topic] = 0 
#             count = 0  

#         for chapter_main in chapters:
#             if chapter_main in temp:
#                 grouped_data[test][topic] += temp[chapter_main]
#                 count += 1

#         if count > 0:
#             grouped_data[test][topic] = round(grouped_data[test][topic] / count, 2)
#     student_grouped_data=grouped_data

#     grouped_data = {}
#     test_data=class_data[-1]
#     test = list(test_data.keys())[0]
#     temp = test_data[test][f'Avg_of_class_chapter_wise']
    
#     if test not in grouped_data:
#         grouped_data[test] = {}

#     for topic, chapters in subjects[subject].items():
#         if topic not in grouped_data[test]:
#             grouped_data[test][topic] = 0 
#             count = 0  

#         for chapter_main in chapters:
#             if chapter_main in temp:
#                 grouped_data[test][topic] += temp[chapter_main]
#                 count += 1

#         if count > 0:
#             grouped_data[test][topic] = round(grouped_data[test][topic] / count, 2)
#     class_grouped_data=grouped_data

#     print(student_grouped_data)
#     student_data_processing=list(student_grouped_data.values())[0]
#     student_label=list(student_data_processing.keys())
#     student_values=list(student_data_processing.values())
#     fig = plt.figure(figsize=(7, 7))
#     ax = fig.add_subplot()

#     # Create the Pie Chart
#     ax.pie(student_values, labels=student_label, autopct='%1.1f%%', startangle=140)

#     # Save as PNG
#     plt.savefig("student_pie_chart.png", dpi=300)

#     # Show the figure
#     plt.show()
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
    a,b=get_data(data_processed_path,common_data_processed_path)
    # generate_grayscale_heatmaps(a,b)
    # student_class_avg_datewise(a,b)
    # plot_student_vs_class_avg_spi(a,b)
    # print(group_by_topics(a, "PHYSICS", "student"))
    create_pie_chart_for_distribution_comparison(a,b)