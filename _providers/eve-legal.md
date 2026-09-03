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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eve-legal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eve.legal
- group: other
  title: ''
  type: ParentCompany
  url: https://www.eve.legal/about-us
- group: company
  title: ''
  type: About
  url: https://www.eve.legal/about-us
- group: other
  title: ''
  type: Product
  url: https://www.eve.legal/eve-2
- group: other
  title: ''
  type: Agents
  url: https://www.eve.legal/eve-agents
- group: other
  title: ''
  type: Auditor
  url: https://www.eve.legal/eve-auditor
- group: other
  title: ''
  type: PracticeArea
  url: https://www.eve.legal/personal-injury
- group: other
  title: ''
  type: PracticeArea
  url: https://www.eve.legal/labor-and-employment
- group: other
  title: ''
  type: CustomerStories
  url: https://www.eve.legal/customer-stories
- group: build
  title: ''
  type: ResourceLibrary
  url: https://www.eve.legal/resource-library
- group: company
  title: ''
  type: Blog
  url: https://www.eve.legal/blog
- group: company
  title: ''
  type: Press
  url: https://www.eve.legal/press
- group: learn
  title: ''
  type: Webinars
  url: https://www.eve.legal/webinars
- group: other
  title: ''
  type: AINativeLawFirms
  url: https://www.eve.legal/ai-native-law-firms
- group: company
  title: ''
  type: Careers
  url: https://www.eve.legal/careers
- group: other
  title: ''
  type: ReferAFirm
  url: https://www.eve.legal/refer-a-firm
- group: start
  title: ''
  type: Demo
  url: https://www.eve.legal/schedule-a-call
- group: start
  title: ''
  type: Login
  url: https://app.eve.legal
- group: commercial
  title: ''
  type: MasterServiceAgreement
  url: https://www.eve.legal/master-service-agreement
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.eve.legal/service-level-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eve.legal/privacy
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/eve-legal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eve-legal
created: '2026-05-25'
description: 'Eve (eve.legal) is a legal AI platform built by Butler Labs, Inc. for plaintiff law firms. Marketed as "the only legal AI that works your whole case with you," Eve 2.0 is positioned as a proactive AI workforce that spans the full plaintiff case lifecycle — intake and evaluation, pre-litigation drafting (medical chronologies, demand letters), litigation discovery (propounding and responding), and case auditing. The platform is organized around three product surfaces: Eve Agents (intake & evaluation, AI voice agent, medical overviews, demand letters, drafting, propounding discovery, responding to discovery), Eve Auditor (nightly audit of the active caseload for missed value drivers such as TBIs, MRIs ordered but not taken, and mass-tort eligibility), and Eve Analyst (announced as "coming soon"). Eve targets personal injury and labor & employment plaintiff firms and claims to be used by 1000+ firms with reported outcomes including a 250% year-over-year revenue increase, 2.5x case
  capacity, 90% faster demand letter generation, and a 4.9/5 G2 rating. Eve is SOC 2 Type 2 certified and HIPAA compliant, with case data encrypted, isolated per-firm, and never used to train shared models. The company is led by founder & CEO Jay Madheswaran (formerly Rubrik, Lightspeed Venture Partners), co-founder & CPO Matt Noe, and co-founder & Head of Engineering David Zeng, and has raised $164M+ from venture investors. Eve is a closed B2B SaaS application; as of this profile there is no public developer API, no public OpenAPI/AsyncAPI documentation, no `docs.eve.legal` developer portal, no SDKs, and no public repositories under the `eve-legal` GitHub organization (the org exists with zero public repos as of May 2026). All access is through the Eve web application following a sales-led "Schedule a call" / "Book a Demo" motion.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eve-legal.png
layout: provider
modified: '2026-05-25'
name: Eve
nav: Providers
network: true
overview: 'Eve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal AI, Legal Technology, Plaintiff Law, Personal Injury, and Labor And Employment.


  Eve''s developer surface includes engineering blog and 23 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eve-legal/refs/heads/main/screenshots/eve-legal-2026-06-20T180853.png
security:
- kind: domain-security
  name: Eve Legal Domain Security
  slug: eve-legal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eve-legal
tags:
- Legal AI
- Legal Technology
- Plaintiff Law
- Personal Injury
- Labor And Employment
- Case Intake
- Demand Letters
- Medical Chronology
- Discovery
- Litigation
- Document Drafting
- AI Agents
- Voice Agent
- Case Auditing
- Software-as-a-Service
- SOC 2
- HIPAA
- Butler Labs
website: https://www.eve.legal
---
