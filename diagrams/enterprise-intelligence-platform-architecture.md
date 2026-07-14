# Enterprise Intelligence Platform Architecture

```mermaid
graph TD
    ACP[Agentic Control Plane]

    ACP --> EIP[Enterprise Intelligence Platform]

    EIP --> AA[Analytics Agent]
    EIP --> FA[Forecasting Agent]
    EIP --> AN[Anomaly Agent]
    EIP --> IA[Insights Agent]

    AA --> WF[Intelligence Workflow]
    FA --> WF
    AN --> WF
    IA --> WF

    WF --> EI[Enterprise Intelligence Engine]
