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
- description: 'The public WordPress REST API (wp-json) of the Arbor Biotechnologies website at arbor.bio: the route index of the site''s content management system, catalogued as one site surface rather than as separa'
  name: Arbor Biotechnologies Website (WordPress REST)
  slug: arbor-bio-website-wordpress-rest
artifact_total: 4
collections:
- collection_type: open
  name: Arbor Biotechnologies Content API (WordPress REST)
  slug: open-arbor-biotechnologies-content
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/overlays/arbor-biotechnologies-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/arbor-biotechnologies-content-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/security/arbor-biotechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arbor-biotechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arbor.bio/
- group: company
  title: ''
  type: Blog
  url: https://arbor.bio/stay-updated/
- group: company
  title: ''
  type: BlogRSS
  url: https://arbor.bio/feed/
- group: company
  title: ''
  type: About
  url: https://arbor.bio/who-we-are/
- group: other
  title: ''
  type: Founders
  url: https://arbor.bio/who-we-are/founders/
- group: other
  title: ''
  type: Leadership
  url: https://arbor.bio/who-we-are/leadership/
- group: company
  title: ''
  type: Investors
  url: https://arbor.bio/who-we-are/investors/
- group: company
  title: ''
  type: Partners
  url: https://arbor.bio/who-we-are/partnerships/
- group: other
  title: ''
  type: Technology
  url: https://arbor.bio/what-we-do/
- group: other
  title: ''
  type: Publications
  url: https://arbor.bio/what-we-do/scientific-publications/
- group: other
  title: ''
  type: Pipeline
  url: https://arbor.bio/pipeline/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://arbor.bio/clinical-trial/
- group: company
  title: ''
  type: Careers
  url: https://arbor.bio/inside-arbor/careers/
- group: operate
  title: ''
  type: Contact
  url: https://arbor.bio/get-in-touch/
- group: operate
  title: ''
  type: Support
  url: https://arbor.bio/get-in-touch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arbor.bio/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arbor.bio/terms-of-use/
- group: other
  title: ''
  type: SiteMap
  url: https://arbor.bio/site-map/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arborbio
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/arbortx
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/arbor-biotechnologies_stock/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/llms/arbor-biotechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arbor-biotechnologies-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/authentication/arbor-biotechnologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arbor-biotechnologies-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/conventions/arbor-biotechnologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arbor-biotechnologies-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/errors/arbor-biotechnologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arbor-biotechnologies-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/data-model/arbor-biotechnologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arbor-biotechnologies-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/lifecycle/arbor-biotechnologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/arbor-biotechnologies-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/conformance/arbor-biotechnologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arbor-biotechnologies-conformance.yml
created: '2026-07-31'
description: Arbor Biotechnologies is a next-generation gene editing company founded in 2016 by Feng Zhang, David Walt, David Scott and Winston Yan, and headquartered in Cambridge, Massachusetts. Its proprietary AI- and machine-learning-guided discovery engine has produced a toolbox of programmable DNA editors spanning knockdown, nuclease excision and compact reverse-transcriptase editing, aimed at functionally curative genomic medicines. The wholly-owned pipeline is focused on liver disease (ABO-101 for primary hyperoxaluria type 1 and ABO-103, both LNP-delivered and partnered with Chiesi Group) and CNS disease (ABO-202, ABO-203 and ABO-204 for ALS, plus ABO-206, all AAV-delivered), alongside collaborative ex vivo cell therapy programs run with Vertex, Allogene, Edigene and Chiesi. Investors include ARCH Venture Partners, Ally Bridge Group, Temasek, TCG and the Samsung Life Science Fund. Arbor operates no product or developer API and publishes no developer portal, SDKs or API documentation;
  its corporate site does serve the standard WordPress REST API anonymously, which makes its press releases, site pages and taxonomies machine-readable.
image: https://arbor.bio/wp-content/uploads/Transparent-Color-Logo-1.png
layout: provider
modified: '2026-07-31'
name: Arbor Biotechnologies
nav: Providers
network: true
overview: 'Arbor Biotechnologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Editing, CRISPR, and Genomic Medicine.


  Arbor Biotechnologies'' developer surface includes engineering blog, support, authentication, and 28 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 30.4
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 18.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/screenshots/arbor-biotechnologies-2026-08-07T161620.png
security:
- kind: authentication
  name: Arbor Biotechnologies Authentication
  slug: arbor-biotechnologies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arbor Biotechnologies Domain Security
  slug: arbor-biotechnologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arbor-biotechnologies
tags:
- Company
- Biotechnology
- Gene Editing
- CRISPR
- Genomic Medicine
- Life Sciences
- Drug Development
- Clinical Trials
- Neurology
- Rare Disease
- Healthcare
- Private Company
website: https://arbor.bio/
---
