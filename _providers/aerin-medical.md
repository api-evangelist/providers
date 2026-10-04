---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Aerin Medical website at aerinmedical.com: the route index of the site''s content management system, catalogued as one site surface rather than as separat'
  name: Aerin Medical Website (WordPress REST)
  slug: aerinmedical-com-website-wordpress-rest
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://aerinmedical.com/
- group: company
  title: ''
  type: About
  url: https://aerinmedical.com/company/about-us/
- group: company
  title: ''
  type: Blog
  url: https://aerinmedical.com/company/news-and-media/
- group: company
  title: ''
  type: News
  url: https://aerinmedical.com/company/news-and-media/
- group: operate
  title: ''
  type: Support
  url: https://aerinmedical.com/contact-us/
- group: operate
  title: ''
  type: Contact
  url: https://aerinmedical.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://aerinmedical.com/company/careers/
- group: other
  title: ''
  type: Leadership
  url: https://aerinmedical.com/company/leadership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aerinmedical.com/general-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aerinmedical.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://aerinmedical.com/cybersecurity/
- group: auth
  title: ''
  type: Compliance
  url: https://aerinmedical.com/compliance/
- group: other
  title: ''
  type: Patents
  url: https://aerinmedical.com/patents/
- group: docs
  title: ''
  type: Documentation
  url: https://aerinmedical.com/ifu/
- group: other
  title: ''
  type: SafetyInformation
  url: https://aerinmedical.com/important-safety-information/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AerinMedical
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aerin-medical
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AerinMedical
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/aerinmedical
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/aerinmedical/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/aerin-medical_stock/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/well-known/aerin-medical-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aerin-medical-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/security/aerin-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerin-medical-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/security/aerin-medical-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aerin-medical-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/authentication/aerin-medical-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aerin-medical-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/llms/aerin-medical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerin-medical-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/conventions/aerin-medical-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aerin-medical-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/errors/aerin-medical-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aerin-medical-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/data-model/aerin-medical-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aerin-medical-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/lifecycle/aerin-medical-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aerin-medical-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/conformance/aerin-medical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aerin-medical-conformance.yml
created: '2026-07-31'
description: 'Aerin Medical, Inc. is a privately held medical-device company at 2565 Leghorn Street, Mountain View, California, with a Singapore entity at 60 Albert Street. It develops temperature-controlled radiofrequency devices that let ear, nose and throat physicians treat chronic nasal conditions in the office under local anesthetic, without incisions: the VivAer Stylus for nasal airway obstruction and the RhinAer Stylus for chronic rhinitis, both FDA-cleared and delivered through the Aerin Console. More than 200,000 patients have been treated as of March 2026. Aerin Medical operates no developer API programme — no portal, no documentation, no keys, no SDKs, no MCP server, no agent card and no status page. Its corporate site does serve an anonymously readable WordPress REST API, and one namespace of it is a genuinely useful first-party dataset: the doctor finder behind aerinmedical.com/find-ent-doctor/, which returns 1,012 treating ENT locations with coordinates and supports free-text,
  proximity, product and Center of Excellence filters. The company also publishes a real Coordinated Vulnerability Disclosure Policy for the Aerin Console, though it is not advertised at /.well-known/security.txt.'
image: https://aerinmedical.com/wp-content/uploads/2020/02/Aerin_Logo-01.png
layout: provider
modified: '2026-07-31'
name: Aerin Medical
nav: Providers
network: true
overview: 'Aerin Medical publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, ENT, and Otolaryngology.


  Aerin Medical''s developer surface includes engineering blog, product news, support, documentation, authentication, and 27 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 67.0
    operational_transparency: 13.2
  previous_composite: 24.1
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/aerin-medical/refs/heads/main/screenshots/aerin-medical-2026-08-07T160959.png
security:
- kind: authentication
  name: Aerin Medical Authentication
  slug: aerin-medical-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Aerin Medical Domain Security
  slug: aerin-medical-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aerin Medical Vulnerability Disclosure
  slug: aerin-medical-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aerin-medical
tags:
- Company
- Medical Devices
- Healthcare
- ENT
- Otolaryngology
- Rhinology
- Radiofrequency Ablation
- Nasal Airway Obstruction
- Chronic Rhinitis
- Physician Locator
- Private Company
website: https://aerinmedical.com/
---
