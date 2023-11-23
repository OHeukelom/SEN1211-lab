from boltzmann_wealth_model.model import BoltzmannWealthModel

# Initialize model
test_model = BoltzmannWealthModel(50, 10, 10)
# Run the model for 3 steps
test_model.run_model(100)

gini_change = test_model.datacollector.get_model_vars_dataframe()
print(gini_change)