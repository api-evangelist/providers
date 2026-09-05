---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 17
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/abridge-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abridge-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abridge-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abridge-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.abridge.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/abridge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abridge-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abridge-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abridgeai
- group: company
  title: ''
  type: Website
  url: https://www.abridge.com/
- group: other
  title: ''
  type: CustomerHub
  url: https://hub.abridge.com/
- group: operate
  title: ''
  type: Support
  url: https://support.abridge.com/
- group: company
  title: ''
  type: Press
  url: https://www.abridge.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.abridge.com/blog
- group: other
  title: ''
  type: Research
  url: https://www.abridge.com/research
- group: operate
  title: ''
  type: Contact
  url: https://www.abridge.com/contact
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/Abridge
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abridge-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AbridgeHQ
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abridge.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abridge.com/privacy
- group: other
  title: ''
  type: Customers
  url: ''
- group: build
  title: ''
  type: IntegrationModel
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Recognition
  url: ''
coverage:
  checked: '2026-08-15'
  detail: Abridge ships ambient clinical documentation as an in-EHR end-user product — abridge.com has no developer, API or docs section at all (every /api, /developers and /openapi.json path returns the Webflow 404 page, and the 544-URL sitemap contains none), no api./developer./docs host serves a spec (docs.abridge.com is only a Google Workspace redirect for staff), and the only /.well-known/ 200s on Abridge hosts belong to its vendors Atlassian and SafeBase, not to Abridge; third-party integration is brokered by Epic's Partners and Pals program instead.
  evidence:
  - status: 404
    url: https://www.abridge.com/developers
  - status: 404
    url: https://www.abridge.com/openapi.json
  - status: 404
    url: https://www.abridge.com/.well-known/agent-card.json
  - status: 302
    url: http://docs.abridge.com/
  - status: 401
    url: https://hub.abridge.com/
  reason: no-developer-program
  state: none
created: '2026-05-23'
description: Abridge provides enterprise-grade generative AI for clinical conversations, transforming patient-clinician interactions into contextually aware, clinically useful, and billable AI-generated notes. Its Contextual Reasoning Engine powers ambient documentation embedded directly in the Epic EHR (Abridge Inside), with deployments across more than 100 health systems including Mayo Clinic, UPMC, Kaiser Permanente, Johns Hopkins, and Duke Health. Abridge reaches third-party developers and EHR partners through Epic's Partners and Pals program rather than a public, self-service developer API.
features:
- description: Real-time AI-generated clinical notes from patient-clinician conversations.
  name: Ambient Clinical Documentation
- description: Proprietary healthcare AI infrastructure underpinning Abridge's documentation and reasoning products.
  name: Contextual Reasoning Engine
- description: Direct in-EHR experience embedded into Epic from Haiku to Hyperdrive, delivering ambient documentation inside the existing clinician workflow.
  name: Abridge Inside
- description: Closes revenue cycle gaps at the point of conversation with coding-ready notes.
  name: Revenue Cycle
- description: AI-powered ambient documentation for nursing teams developed in partnership with Mayo Clinic and Epic.
  name: Nursing Documentation
- description: Expansion of ambient documentation into inpatient settings as part of the Epic partnership.
  name: Inpatient Care
- description: Coverage including Abridge Inside for Emergency Medicine and other specialty workflows.
  name: Specialty Coverage
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abridge.png
integrations:
- description: First Pal in Epic's Partners and Pals program and participant in Epic's Workshop co-development program; Abridge Inside is embedded across Epic Haiku and Hyperdrive.
  name: Epic
layout: provider
modified: '2026-08-15'
name: Abridge
nav: Providers
network: true
overview: 'Abridge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Ambient AI, Clinical Documentation, Generative AI, and Revenue Cycle.


  Abridge''s developer surface includes support, engineering blog, and 19 more developer resources.'
plans:
- name: Abridge Plans Pricing
  plan_count: 0
  slug: abridge-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Abridge Rate Limits
  slug: abridge-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 20.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abridge/refs/heads/main/screenshots/abridge-2026-06-20T163318.png
security:
- kind: domain-security
  name: Abridge Domain Security
  slug: abridge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Abridge Trust Center
  slug: abridge-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, HIPAA, CCPA, TX-RAMP, WCAG
slug: abridge
tags:
- Healthcare
- Ambient AI
- Clinical Documentation
- Generative AI
- Revenue Cycle
- Nursing Documentation
- EHR Integration
- Epic
use_cases:
- description: Generating ambient notes during outpatient visits across primary care and specialties.
  name: Outpatient Clinical Documentation
- description: Ambient documentation for inpatient clinicians and care teams.
  name: Inpatient Clinical Documentation
- description: Workflow-tuned documentation for emergency departments.
  name: Emergency Medicine Documentation
- description: Generative AI to reduce nursing documentation burden.
  name: Nurse Workflow Support
- description: Auto-generated, audit-ready notes that strengthen coding and billing.
  name: Revenue Cycle Capture
website: https://www.abridge.com/
---
