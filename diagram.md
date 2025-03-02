```mermaid
graph TD

subgraph Data_Preparation
  A[Voter Data\n(Name + Address)] --> D[Race Prediction Model\n(NLP + Geolocation Data)]
  B[Raw Real Estate Data\n(NY Counties)] --> C[Data Cleaning Process\n(NLP Model + Regex, iterative)]
  C --> E[Cleaned Data\n(Standardized Names)]
end

D --> F[Predicted Race per Individual]
E --> F

F --> G[Aggregate Race Predictions\n(Summarize Property Ownership by Census Tract)]
G --> H[Compare Predicted Ownership with Actual Census Data\n(Identify Net Renters and Landlords by Race)]
H --> I[Prediction Error Model\n(Geolocationally-correlated uncertainty estimation)]
I --> J[Evaluate Impact of Prediction Uncertainty\n(Assess robustness of conclusions)]
```
