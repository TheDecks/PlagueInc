from classes.town import Town
import matplotlib.pyplot as plt


zurich = Town(no_homes=1000, contamination_length=2)
zurich.create_homes()
zurich.create_schools()
zurich.create_work_places()
zurich.create_shopping_centres()
zurich.create_meeting_places()
zurich.create_gyms()
zurich.create_agents(
    adult_ill_transfer_probability=0.005,
    child_ill_transfer_probability=0.02,
    adult_recover_probability=0.1,
    child_recover_probability=0.05
)
zurich.assign_work_places_and_schools()
zurich.assign_extracurricular_activities()
zurich.spread_virus(0.05)
for _ in range(8 * 7 * 24):
    zurich.update_timers()

fig, ax = plt.subplots()
ax.plot(zurich.recovered_reports)
ax.plot(zurich.sick_reports)
ax.plot(zurich.susceptible_reports)
occ = []
for home in zurich.homes:
    occ.append(home.occupancy_report)

occ_avg = []
for vals in zip(*occ):
    occ_avg.append(sum(vals)/len(vals))
fig, ax = plt.subplots()
ax.plot(occ_avg)
plt.show()
