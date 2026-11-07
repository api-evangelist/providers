---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'REST API for ambient clinical documentation: upload audio or open a WebSocket stream, generate structured SOAP / custom-template clinical notes, extract medical codes (ICD-10, CPT, SNOMED), and receiv'
  name: Sully AI Scribe API
  slug: scribe
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/sully-ai/plans/sully-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sully-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sully.ai/
- group: agent
  href: https://artifacts.apis.io/sully-ai/llms/sully-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sully-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/sully-ai/a2a/sully-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sully-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/sully-ai/well-known/sully-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sully-ai-status-security.txt
- group: agent
  href: https://artifacts.apis.io/sully-ai/well-known/sully-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sully-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/sully-ai/hosts/sully-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sully-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/sully-ai/integrations/sully-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/sully-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/sully-ai/vendors/sully-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sully-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/sully-ai/packages/sully-ai-packages.yml
  title: ''
  type: Packages
  url: packages/sully-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sully.ai/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sully.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.sully.ai/help-center/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sully.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.sully.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.sully.ai/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sully.ai/help-center/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.sully.ai/release-notes
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sully.ai`
- group: auth
  href: https://artifacts.apis.io/sully-ai/security/sully-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sully-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sully-ai/security/sully-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sully-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sully.ai
- group: company
  title: ''
  type: AboutUs
  url: https://www.sully.ai/about-us
- group: other
  title: ''
  type: Products
  url: https://www.sully.ai/products
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sully.ai
- group: company
  title: ''
  type: Blog
  url: https://www.sully.ai/blog
- group: other
  title: ''
  type: Labs
  url: https://www.sully.ai/labs
- group: operate
  title: ''
  type: Contact
  url: https://www.sully.ai/demo-em
- group: operate
  title: ''
  type: Support
  url: mailto:support@sully.ai
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sullyai
coverage:
  checked: '2026-10-29'
  detail: Documentation exists but no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://docs.sully.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-24'
description: Sully AI is a US-based healthcare AI company that ships a portfolio of "AI employees" for clinical and administrative work — including an AI Scribe that turns patient conversations into structured, HIPAA-compliant notes, an AI Receptionist for scheduling and front desk, an AI Triage Nurse for patient engagement, an AI Medical Coder for autonomous ICD-10 coding, an AI Pharmacist, and an AI Consultant for chart prep. The platform integrates with Epic, Cerner, MEDITECH, Athenahealth, Allscripts, Veradigm, and 50+ other EHRs. Beyond the end-user products, Sully exposes a public REST API covering audio transcription (file upload and real-time WebSocket streaming), clinical note generation (SOAP and custom templates), medical coding extraction (ICD-10, CPT, SNOMED), note templates, and a medical consensus alpha feature, with asynchronous results delivered over webhooks. Official Apache-2.0 licensed TypeScript/Node and Python SDKs are published under the sullyai GitHub org, and an
  Odiggo-maintained sully-api-demo repo showcases end-to-end usage. Sully's revenue model is SaaS subscriptions to healthcare providers, hospitals, and digital health platforms.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sully-ai.png
layout: provider
modified: '2026-05-24'
name: Sully AI
nav: Providers
network: true
overview: 'Sully AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Health Tech, Medical AI, Clinical AI, and AI Scribe.


  Sully AI''s developer surface includes pricing, getting-started guide, changelog, documentation, engineering blog, support, GitHub presence, and 23 more developer resources.'
plans:
- name: Sully Ai Plans Pricing
  plan_count: 5
  slug: sully-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Sully Ai Rate Limits
  slug: sully-ai-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 46.4
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 43.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sully-ai/sully-ai-2026-06-20T194647.png
security:
- kind: domain-security
  name: Sully Ai Domain Security
  slug: sully-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sully Ai Trust Center
  slug: sully-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: sully-ai
tags:
- Healthcare
- Health Tech
- Medical AI
- Clinical AI
- AI Scribe
- Ambient Scribe
- Clinical Documentation
- SOAP Notes
- Medical Coding
- ICD-10
- CPT
- SNOMED
- Speech-to-Text
- Audio Transcription
- Real-Time Streaming
- WebSocket
- Webhook
- EHR Integration
- Epic
- Cerner
- HIPAA
- AI Agents
- Workflow Automation
- Healthcare Automation
website: https://www.sully.ai
---
