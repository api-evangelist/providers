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
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abbott-laboratories-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abbott-
- group: company
  title: ''
  type: Website
  url: https://www.abbott.com/
- group: company
  title: ''
  type: Partners
  url: https://www.abbott.com/en-us/partners.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abbott.com/en-us/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abbott.com/en-us/online-terms-and-conditions.html
- group: operate
  title: ''
  type: Contact
  url: https://www.abbott.com/en-us/about-abbott/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.abbott.com/corpnewsroom.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abbott-laboratories-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/abbott-laboratories-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abbott-laboratories-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/abbott-laboratories-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/abbott-laboratories-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/abbott-laboratories-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abbott-laboratories-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/abbott-laboratories-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/abbott-laboratories-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abbott-laboratories-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abbott-laboratories-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: 'Abbott''s one real API — the LibreView cloud API behind FreeStyle Libre and LibreLinkUp — has no public reference at all: access is granted only through a partner agreement negotiated directly with Abbott Diabetes Care, and the page apis.yml carried as Abbott''s developer portal turns out to be a supplier-and-licensing page that names no API, SDK or documentation anywhere on it.'
  evidence:
  - status: 200
    url: https://www.abbott.com/en-us/partners.html
  - status: 404
    url: https://api.libreview.io/openapi.json
  - status: 403
    url: https://www.abbott.com/.well-known/api-catalog
  - status: 404
    url: https://www.abbott.com/llms.txt
  reason: sales-gate
  state: gated
created: '2024-01-15'
description: Abbott Laboratories is a global healthcare company that develops, manufactures, and markets pharmaceuticals, medical devices, diagnostics, and nutritional products. Abbott's digital health portfolio includes the FreeStyle Libre continuous glucose monitoring system, cardiac monitoring devices, and connected diagnostics platforms that enable data sharing between patients, caregivers, and healthcare providers.
features:
- description: Continuous glucose monitoring system with LibreLinkUp connectivity for real-time glucose data sharing
  name: FreeStyle Libre CGM
- description: Point-of-care and laboratory diagnostics for infectious disease, cardiac, and metabolic conditions
  name: Diagnostics Platforms
- description: Cardiac monitoring devices including implantable monitors and remote patient monitoring
  name: Connected Heart Monitoring
- description: Science-based nutritional products across adult and pediatric segments
  name: Nutrition Products
- description: Branded generic medicines across cardiometabolic, women's health, and gastroenterology
  name: Pharmaceutical Technologies
image: /assets/icons/abbott-laboratories.png
integrations:
- description: Mobile app ecosystem for sharing FreeStyle Libre glucose data with caregivers
  name: LibreLinkUp
- description: Integration with major EHR platforms for clinical data exchange
  name: Electronic Health Records
- description: Integration with Apple HealthKit for sharing device data on iOS
  name: Apple Health
- description: Integration with Google Health for sharing device data on Android
  name: Google Health
layout: provider
modified: '2026-08-29'
name: Abbott Laboratories
nav: Providers
network: true
overview: 'Abbott Laboratories is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Medical Devices, Diagnostics, Digital Health, and Life Sciences.


  Abbott Laboratories'' developer surface includes engineering blog and 18 more developer resources.'
plans:
- name: Abbott Laboratories Plans Pricing
  plan_count: 0
  slug: abbott-laboratories-plans-pricing
press:
- date: '2026-05-25'
  title: Abbott receives FDA clearance, CE Mark for AI imaging ...
  url: https://www.investing.com/news/company-news/abbott-receives-fda-clearance-ce-mark-for-ai-imaging-platform-93CH-4641583
- date: '2026-05-25'
  title: 'Abbott''s AI Strategy: Analysis of AI Dominance in Medical ...'
  url: https://www.klover.ai/abbott-ai-strategy-analysis-of-ai-dominance-in-medical-devices-healthcare/
- date: '2026-05-25'
  title: Artificial Intelligence at Abbott - Two Current Use-Cases
  url: https://emerj.com/artificial-intelligence-at-abbott/
- date: '2026-05-25'
  title: Douglas Lautner Ph.D. - Senior Director of Artificial ...
  url: https://www.linkedin.com/in/douglaslautner
- date: '2026-05-25'
  title: Abbott Reports First-Quarter 2026 Results; Updates ...
  url: https://www.prnewswire.com/news-releases/abbott-reports-first-quarter-2026-results-updates-guidance-to-reflect-acquisition-of-exact-sciences-302744652.html
random_paper: 15
rate_limits:
- limit_count: 0
  name: Abbott Laboratories Rate Limits
  slug: abbott-laboratories-rate-limits
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 12
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 21.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abbott-laboratories/refs/heads/main/screenshots/abbott-laboratories-2026-06-20T163122.png
security:
- kind: domain-security
  name: Abbott Laboratories Domain Security
  slug: abbott-laboratories-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Abbott Laboratories Vulnerability Disclosure
  slug: abbott-laboratories-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Abbott Laboratories Trust Center
  slug: abbott-laboratories-trust-center
  summary_line: French ASIP Santé / HDS (Hébergeur de Données de Santé — Health Data Host), EU-U.S. Data Privacy Framework
slug: abbott-laboratories
tags:
- Healthcare
- Medical Devices
- Diagnostics
- Digital Health
- Life Sciences
- Fortune 500
use_cases:
- description: Connect continuous glucose monitors and cardiac devices to enable remote health tracking
  name: Remote Patient Monitoring
- description: Integrate Abbott device data with electronic health records and care management platforms
  name: Digital Health Integration
- description: Streamline laboratory and point-of-care testing workflows with Abbott diagnostic systems
  name: Clinical Diagnostics
- description: Build applications that integrate with FreeStyle Libre and other Abbott connected devices
  name: Companion App Development
website: https://www.abbott.com/
---
