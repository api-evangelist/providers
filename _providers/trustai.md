---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://trytrust.ai'', ''status'': 308, ''note'': ''declared website redirects to https://onetriangle.ai/ — a different registrable domain (trytrust.ai -> onetriangle.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trytrust.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trytrust.ai/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trytrust.ai/legal/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/autotrytrustai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/TryTrustAI
created: '2026-07-17'
description: TrustAI (trytrust.ai) is a San Francisco-based Y Combinator Summer 2026 company founded in 2026 by Hannah Chung and Medha Venkatapathy that provides continuous compliance, governance, and risk assessment for AI agents operating on sensitive enterprise systems, with an initial focus on ERP agents such as SAP Joule. It maps what every agent can reach, then runs evaluations across six domains - data privacy, hallucinations and grounding, permission compliance, robustness at scale, accountability, and security - including adversarial pentests and prompt-injection red-teaming, and maps every risk to controls like SOX, ITGC, ISO 27001, GxP, and the EU AI Act for audit-ready reporting. The company does not currently publish a public developer API, docs, or SDKs. This profile was added to the API Evangelist network as a portfolio-lead stub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustai.png
layout: provider
modified: '2026-07-21'
name: TrustAI
nav: Providers
network: true
overview: TrustAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Governance, and Compliance.
random_paper: 3
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trustai/refs/heads/main/screenshots/trustai-2026-09-02T164417.png
security:
- kind: domain-security
  name: Trustai Domain Security
  slug: trustai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: trustai
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Governance
- Compliance
- Security
- Risk Assessment
- ERP
- B2B
website: https://trytrust.ai
---
