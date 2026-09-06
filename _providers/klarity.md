---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.klarity.ai'', ''status'': 307, ''note'': ''declared website redirects to https://www.within.ai/ — a different registrable domain (klarity.ai -> within.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klarity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.klarity.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.klarity.ai/docs/home
- group: start
  title: ''
  type: GettingStarted
  url: https://www.klarity.ai/docs/user-docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.klarity.ai/resources/blog
- group: docs
  title: ''
  type: Guides
  url: https://www.klarity.ai/resources/guides
- group: start
  title: ''
  type: SignUp
  url: https://www.klarity.ai/request-demo
- group: start
  title: ''
  type: Login
  url: https://app.klarity.ai/
- group: company
  title: ''
  type: Partners
  url: https://www.klarity.ai/partners
- group: company
  title: ''
  type: About
  url: https://www.klarity.ai/about
- group: company
  title: ''
  type: Careers
  url: https://www.klarity.ai/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klarity.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klarity.ai/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.klarity.ai/legal/trust-and-safety
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.klarity.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klarity-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klarity-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klarity-conformance.yml
created: '2026-07-17'
description: 'Klarity is an enterprise AI company behind Klarity Architect, the "Enterprise Instinct Platform" — a Context Graph that captures how work actually happens inside a large organization and turns it into a living operational digital twin. The platform runs in three phases: Discover (an AI Companion that observes work, an AI Interviewer, and bulk file upload capture documented and undocumented processes), Structure (AI mapping organizes what it finds into a multi-level, role-aware Process Index from value streams down to individual activities), and Improve (an Advisor agent surfaces ROI-ranked recommendations and Signals detect drift from an approved standard). Klarity is used for finance, IT, GTM, HR and operations transformation, audit and compliance documentation, automation assessment, and SOP/PDD generation, with customers including DoorDash, Stripe, Salesforce and Uber. The product is delivered as a SaaS workspace with SAML SSO and fine-grained access control; Klarity publishes
  user documentation and an llms.txt index but no public developer API, SDKs, or webhook surface at the time of this profile.'
image: https://klarity.ai/api/og?title=Transforming%20Transformation.&description=The%20Enterprise%20Instinct%20Platform.%20Discover.%20Structure.%20Improve.
layout: provider
modified: '2026-07-19'
name: Klarity
nav: Providers
network: true
overview: 'Klarity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Business Process Management, Process Intelligence, and Enterprise Software.


  Klarity''s developer surface includes documentation, getting-started guide, engineering blog, signup flow, and 14 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klarity/refs/heads/main/screenshots/klarity-2026-07-25T223934.png
security:
- kind: domain-security
  name: Klarity Domain Security
  slug: klarity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Klarity Trust Center
  slug: klarity-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: klarity
tags:
- Company
- Artificial Intelligence
- Business Process Management
- Process Intelligence
- Enterprise Software
- Document Automation
- Finance
- Governance Risk and Compliance
- Agents
website: https://www.klarity.ai
---
