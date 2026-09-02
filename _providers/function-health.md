---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Authenticated member web and mobile dashboard for viewing 100+ lab biomarkers, trends across testing rounds, clinician notes, biological age, and a personalized action plan. There is no documented pub
  name: Function Health Member Dashboard
  slug: function-health-member-dashboard
- description: Member-initiated PDF export of lab results from the documents area of the dashboard. This is a manual download for data portability, not a programmatic API; third-party trackers import the resulting P
  name: Function Health Results Export
  slug: function-health-results-export
- description: In-product Connected Apps let members link supported consumer health services (e.g. wearables and Apple Health) to sync data into Function. These are pre-built, member-authorized integrations configur
  name: Function Health Connected Apps
  slug: function-health-connected-apps
- description: An opt-in app within ChatGPT through which a member can authorize secure access to a limited, high-level summary of their lab results, with the ability to revoke access at any time. Surfaced through t
  name: Function Health ChatGPT App
  slug: function-health-chatgpt-app
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Function Health API
  slug: open-function-health
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/function-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/function-health-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/function-health
- group: company
  title: ''
  type: Website
  url: https://www.functionhealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.functionhealth.com/faqs
- group: commercial
  title: ''
  type: Plans
  url: plans/function-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/function-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/function-health-finops.yml
created: '2026-06-20'
description: Function Health is a consumer longevity and preventive-health membership that runs 100+ lab biomarkers twice a year through Quest Diagnostics, adds clinician review, a biological age calculation, and an AI health companion via a web and mobile dashboard. As of this catalog Function Health does not publish a public or partner developer API; member data is accessed through the member dashboard, PDF export, in-product Connected Apps (wearable sync), and an opt-in ChatGPT app that shares a high-level summary of results.
finops:
- name: Function Health Finops
  service_category: Healthcare
  slug: function-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/function-health.png
layout: provider
modified: '2026-06-20'
name: Function Health
nav: Providers
network: true
overview: 'Function Health publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Member Dashboard, Results Export, Connected Apps, and 1 more. Tagged areas include Health, Longevity, Lab Testing, Biomarkers, and Preventive Health.


  Function Health''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Function Health Plans Pricing
  plan_count: 2
  slug: function-health-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Function Health Rate Limits
  slug: function-health-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Function Health Domain Security
  slug: function-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Function Health Trust Center
  slug: function-health-trust-center
  summary_line: SOC 2, HIPAA
slug: function-health
tags:
- Health
- Longevity
- Lab Testing
- Biomarkers
- Preventive Health
- Consumer Health
website: https://www.functionhealth.com
---
