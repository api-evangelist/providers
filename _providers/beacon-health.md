---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.beaconhealth.ai/
- group: start
  title: ''
  type: Login
  url: https://www.beaconhealth.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beaconhealth.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beaconhealth.ai/privacy
- group: operate
  title: ''
  type: Contact
  url: https://form.typeform.com/to/mJ8w6Xot
- group: company
  title: ''
  type: Crunchbase
  url: https://www.ycombinator.com/companies/beacon-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beacon-health-ai/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beacon-health-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beacon-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beacon-health-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beacon-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.beaconhealth.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/beacon-health-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/beacon-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/beacon-health-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beacon-health-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beacon-health-llms.txt
coverage:
  checked: '2026-08-15'
  detail: Beacon Health ships software but only as a managed service — contract discovery probed 55 paths across www., api. and trust.beaconhealth.ai and found no OpenAPI, GraphQL, MCP or agent card, because the company's stated thesis is that its agents drive EHR user interfaces precisely where no usable API exists.
  evidence:
  - status: 404
    url: https://api.beaconhealth.ai/openapi.json
  - status: 404
    url: https://www.beaconhealth.ai/docs
  - status: 404
    url: https://api.beaconhealth.ai/.well-known/agent-card.json
  - status: 200
    url: https://api.beaconhealth.ai/.well-known/openid-configuration
  - status: 200
    url: https://trust.beaconhealth.ai/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Beacon Health (YC W26) is a San Francisco company building "AI employees" for primary care — autonomous agents that operate directly inside electronic health record systems the same way a human staff member does. Rather than integrating through an EHR vendor API, Beacon records a practice''s existing workflow in the EHR (navigation, clicks, data entry) and converts that recording into a reusable, deployable agent that runs at scale across the whole patient panel. The agents automate value-based-care back-office work: preventative and quality gap closure, pre-charting, prior authorizations, referrals, transition-of-care management, and HCC risk-adjustment coding. Beacon advertises coverage of AthenaHealth, Epic, Cerner, eClinicalWorks, MEDITECH, NextGen, Veradigm Allscripts and MEDENT, plus payer portals and other web applications. Founded in 2025 by Mark Pothen (CEO) and Obinna Akahara (CTO), the company operates as a HIPAA Business Associate under a BAA with each covered entity,
  and publishes a trust center at trust.beaconhealth.ai carrying a 56-control monitored control set, a named eight-vendor subprocessor list, and SOC 2 and HIPAA frameworks both declared in progress with no completed attestation. As of this profile Beacon Health publishes no public developer API, developer portal, API documentation, SDKs, or OpenAPI definition — the product is delivered as a managed agent workforce, not as a self-serve API.'
image: https://www.beaconhealth.ai/apple-touch-icon.png
layout: provider
modified: '2026-08-15'
name: Beacon Health
nav: Providers
network: true
overview: 'Beacon Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, Value Based Care, and EHR.


  Beacon Health''s developer surface includes authentication and 16 more developer resources.'
plans:
- name: Beacon Health Plans Pricing
  plan_count: 0
  slug: beacon-health-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Beacon Health Rate Limits
  slug: beacon-health-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: -1.2
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beacon-health/refs/heads/main/screenshots/beacon-health-2026-07-25T202509.png
security:
- kind: authentication
  name: Beacon Health Authentication
  slug: beacon-health-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Beacon Health Domain Security
  slug: beacon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Beacon Health Vulnerability Disclosure
  slug: beacon-health-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Beacon Health Trust Center
  slug: beacon-health-trust-center
  summary_line: trust center published
slug: beacon-health
tags:
- Company
- Healthcare
- Primary Care
- Value Based Care
- EHR
- Artificial Intelligence
- AI Agents
- Workflow Automation
- Risk Adjustment
- Prior Authorization
- HIPAA
- Y Combinator
website: https://www.beaconhealth.ai/
---
