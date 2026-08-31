---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The APIDynamics platform provides AI-driven API security and observability including API discovery, traffic analysis, real-time risk scoring, adaptive MFA, Zero Trust enforcement, shadow/zombie API de
  name: API Dynamics Platform
  slug: api-dynamics-platform
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-dynamics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apidynamics
- group: company
  title: ''
  type: Website
  url: https://www.apidynamics.com
- group: company
  title: ''
  type: Blog
  url: https://www.apidynamics.com/news
- group: start
  title: ''
  type: Login
  url: https://app.apidynamics.com
- group: start
  title: ''
  type: Signup
  url: https://www.apidynamics.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.apidynamics.com/contact
- group: agent
  title: ''
  type: LlmsText
  url: https://apidynamics.com/llms.txt
created: '2026-03-26'
description: APIDynamics is an AI-driven API security and observability platform that empowers enterprises to gain real-time visibility and secure every API endpoint with intelligent, automated analytics. The platform provides adaptive MFA, real-time risk scoring, Zero Trust enforcement, API discovery, shadow and zombie API detection, BOLA/BFLA detection, sensitive data tracking, and anomaly detection — all within a unified dashboard.
features:
- description: Automatically scan traffic, code, gateways, and ingress to build a complete API inventory with no blind spots, detecting shadow APIs and zombie APIs.
  name: API Discovery
- description: Continuously assess and score API risk in real time using AI and machine learning to analyze traffic patterns and detect anomalies that may indicate an attack.
  name: Real-Time Risk Scoring
- description: Adaptive MFA that adjusts authentication requirements based on risk level, securing every API call including machine-to-machine and non-human interactions.
  name: Adaptive Multi-Factor Authentication
- description: Unified control plane with Zero Trust enforcement ensuring no API call is trusted by default and all requests are continuously validated.
  name: Zero Trust Enforcement
- description: Detect Broken Object Level Authorization (BOLA) and Broken Function Level Authorization (BFLA) vulnerabilities — the top API security risks identified by OWASP.
  name: BOLA and BFLA Detection
- description: Track and monitor sensitive data flowing through API calls to identify data exposure risks and ensure compliance.
  name: Sensitive Data Tracking
- description: AI-powered security analysis that predicts and counters new attack patterns, including security for AI/ML API endpoints.
  name: AI Security for APIs
- description: Embed API security testing and traffic insights into DevOps and CI/CD pipelines for shift-left security practices.
  name: CI/CD Integration
finops:
- name: Api Dynamics Finops
  service_category: API
  slug: api-dynamics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-dynamics.png
layout: provider
modified: '2026-04-19'
name: API Dynamics
nav: Providers
network: true
overview: 'API Dynamics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Security, API Discovery, API Observability, Zero Trust, and API Intelligence.


  API Dynamics'' developer surface includes engineering blog, signup flow, support, and 5 more developer resources.'
plans:
- name: Api Dynamics Plans Pricing
  plan_count: 3
  slug: api-dynamics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Api Dynamics Rate Limits
  slug: api-dynamics-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-dynamics/refs/heads/main/screenshots/api-dynamics-2026-06-20T172204.png
security:
- kind: domain-security
  name: Api Dynamics Domain Security
  slug: api-dynamics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: api-dynamics
tags:
- API Security
- API Discovery
- API Observability
- Zero Trust
- API Intelligence
use_cases:
- description: Continuously assess and improve the security posture of all APIs across the organization using automated scanning and risk scoring.
  name: API Security Posture Management
- description: Discover and remediate shadow APIs and zombie APIs that create security blind spots and compliance risks.
  name: Shadow API Elimination
- description: Implement Zero Trust security for API access with adaptive MFA and continuous verification of every API call.
  name: Zero Trust API Access
- description: Track sensitive data in API traffic to meet compliance requirements and prevent unauthorized data exposure.
  name: Compliance and Data Protection
website: https://www.apidynamics.com
---
