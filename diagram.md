```mermaid
graph TD

subgraph Data Preparation
  A[Voter Data<br>(Name + Address)] --> D[Race Prediction Model<br>(NLP + Geolocation Data)]
  B[Raw Real Estate Data<br>(NY Counties)] --> C[Data Cleaning Process<br>(NLP Model + Regex, iterative)]
  C --> E[Cleaned Data<br>(Standardized Names)]
end

D --> F[Predicted Race per Individual]
E --> F

F --> G[Aggregate Race Predictions<br>(Summarize Property Ownership by Census Tract)]
G --> H[Compare Predicted Ownership with Actual Census Data<br>(Identify Net Renters and Landlords by Race)]
H --> I[Prediction Error Model<br>(Geolocationally-correlated uncertainty estimation)]
I --> J[Evaluate Impact of Prediction Uncertainty<br>(Assess robustness of conclusions)]
