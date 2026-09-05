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
  - '{''url'': ''https://radware.com'', ''status'': 302, ''note'': ''declared website redirects to http://validate.perfdrive.com/?ssa=14bcad6a-611c-4aff-890e-bb09be20aebf&ssb=92855256834&ssc=https%3A%2F%2Fradware.com%2F&ssi=42bb11f7-bsff-434b-a2db-d9b4c5c4ea5f&ssk=support@shieldsquare.com&ssm=42520982706815351101331761234705&ssn=cd6b9f54cec0a097c0b13329e1bbc3e1198b7b5e1f49-47c6-4871-b3f045&sso=fc8d5660-ca1f0c1138b93d376e58b2388b2a06efef9cf348b5d59689&ssp=50753109921788461115178846461273459&ssq=00403795388654169488153886061280010973671&ssr=MTQxLjE1Ny4yMTEuMTk=&sst=APIs.io-website-probe/1.0%20(+https://apis.io)&ssu=&ssv=&ssw=&ssx=eyJyZCI6InJhZHdhcmUuY29tIiwidXpteCI6IjdmYzAwMGZjNjZkYWNlLTc0MDgtNGU1YS05MDM3LTg2NWRjOTM2ZjJlZTEtMTc4ODQ1Mzg4Njg2NzAtMDAzOTlhNGM2YjVmNTAwOWQ3ODEwIiwiX191em1mIjoiN2Y5MDAwN2I1ZTFmNDktNDdjNi00ODcxLWI2NjAtY2ExZjBjMTEzOGI5MS0xNzg4NDUzODg2ODY3MC0wMDQ0YzI3OGRkMDliNGJiYzg0MTAifQ== — a different registrable domain (radware.com -> perfdrive.com), possible rename or acquisition
    (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://radware.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.radware.com/products/alteon/
- group: docs
  title: ''
  type: Documentation
  url: https://support.radware.com/app/answers/answer_view/a_id/16280/~/alteon-rest-api
- group: docs
  title: ''
  type: APIReference
  url: https://portals.radware.com/ProductDocumentation/
- group: operate
  title: ''
  type: Support
  url: https://support.radware.com/
- group: company
  title: ''
  type: Blog
  url: https://www.radware.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Radware
- group: auth
  title: ''
  type: Authentication
  url: authentication/alteon-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/alteon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alteon-packages.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.radware.com/newsroom/certifications/
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/radware
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alteon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alteon-domain-security.yml
created: '2026-07-17'
description: Alteon is Radware's application delivery controller (ADC) and advanced load balancer product line, providing Layer 4-7 load balancing, SSL/TLS offloading, application acceleration, global server load balancing, and integrated application security across on-premises, virtual, and public-cloud environments. Originally Alteon WebSystems (a Matrix Partners-backed company that IPO'd in 1999 and was later acquired by Nortel), the Alteon product line is now developed and supported by Radware. Alteon exposes a device-embedded REST API (accessed at https://<device>/restdoc/, HTTP Basic auth, available from Alteon 34.0.4 / 33.5.8 / 33.0.12 and above) plus first-party automation clients including a Python SDK, a certified Terraform provider, and Ansible modules.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alteon.png
layout: provider
modified: '2026-07-17'
name: Alteon
nav: Providers
network: true
overview: 'Alteon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Application Delivery, Load Balancing, and Application Delivery Controller.


  Alteon''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alteon/refs/heads/main/screenshots/alteon-2026-07-25T195817.png
security:
- kind: authentication
  name: Alteon Authentication
  slug: alteon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alteon Domain Security
  slug: alteon-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Alteon Vulnerability Disclosure
  slug: alteon-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: alteon
tags:
- Company
- Infrastructure
- Application Delivery
- Load Balancing
- Application Delivery Controller
- Application Security
- Networking
- Radware
website: https://radware.com
---
