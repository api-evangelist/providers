---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: Global Privacy Control is a browser-level signal that communicates a user's opt-out preference to websites. The California Attorney General has affirmed that GPC must be treated as a valid CCPA "Do No
  name: Global Privacy Control (GPC) Specification
  slug: global-privacy-control
- description: The IAB Tech Lab Global Privacy Platform (GPP) is the successor to the US Privacy (USP) string. It provides a standardized way to communicate user consent and opt-out signals between publishers, conse
  name: IAB Tech Lab Global Privacy Platform (GPP)
  slug: iab-gpp
- description: Official resources from the California Privacy Protection Agency, the body empowered by CPRA to implement, enforce, and publish regulations under the CCPA.
  name: California Privacy Protection Agency (CPPA) Resources
  slug: cppa-enforcement-resources
- description: Official California Attorney General registry of data brokers required to register under Civil Code section 1798.99.80, providing a public list that consumers can use to submit opt-out requests.
  name: California Data Broker Registry
  slug: ca-data-broker-registry
- baseURL: https://api.drop.privacy.ca.gov
  baseurl_source: declared
  description: The Delete Request and Opt-out Platform (DROP) Data Broker API is the statutory integration surface California's Delete Act requires of every registered data broker. Brokers call GET /data/download to
  name: CalPrivacy DROP Data Broker API
  slug: drop-data-broker-api
artifact_total: 34
asyncapis:
- description: ''
  name: Ccpa Drop Webhooks
  slug: ccpa-drop-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ccpa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ccpa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oag.ca.gov/privacy/ccpa
- group: docs
  title: ''
  type: Documentation
  url: https://oag.ca.gov/privacy/ccpa
- group: other
  title: ''
  type: Regulator
  url: https://cppa.ca.gov/
- group: other
  title: ''
  type: StatuteText
  url: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.5.&part=4.&chapter=&article=
- group: other
  title: ''
  type: Regulations
  url: https://cppa.ca.gov/regulations/
- group: operate
  title: ''
  type: FAQ
  url: https://oag.ca.gov/privacy/ccpa
- group: start
  title: ''
  type: DataBrokerRegistry
  url: https://oag.ca.gov/data-brokers
- group: other
  title: ''
  type: GPC
  url: https://globalprivacycontrol.org/
- group: other
  title: ''
  type: GPP
  url: https://iabtechlab.com/gpp/
- group: other
  title: ''
  type: Rights
  url: ''
- group: other
  title: ''
  type: Applicability
  url: ''
- group: auth
  title: ''
  type: Authentication
  url: authentication/ccpa-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ccpa-drop-databroker-api.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ccpa-drop-databroker-api-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ccpa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ccpa-security.txt
- group: auth
  title: ''
  type: Security
  url: security/ccpa-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ccpa-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ccpa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ccpa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ccpa-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ccpa-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ccpa-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ccpa-drop-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ccpa-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ccpa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ccpa-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ccpa-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ccpa-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ccpa-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ccpa-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://privacy.ca.gov/drop-for-data-brokers/
- group: docs
  title: ''
  type: APIReference
  url: https://privacy.ca.gov/drop-for-data-brokers/technical-specifications/api-operations/
- group: start
  title: ''
  type: GettingStarted
  url: https://privacy.ca.gov/drop-for-data-brokers/technical-specifications/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://privacy.ca.gov/drop-for-data-brokers/help/
- group: company
  title: ''
  type: Blog
  url: https://privacy.ca.gov/about-us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://privacy.ca.gov/drop-for-data-brokers/account-creation-fees-and-annual-registration/
- group: start
  title: ''
  type: SignUp
  url: https://databroker.drop.privacy.ca.gov/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://privacy.ca.gov/conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.ca.gov/privacy-policy/
- group: other
  title: ''
  type: Complaints
  url: https://privacy.ca.gov/submit-a-complaint/ccpa-complaints/
- group: other
  title: ''
  type: LawsAndRegulations
  url: https://privacy.ca.gov/laws-and-regulations/
- group: other
  title: ''
  type: Announcements
  url: https://cppa.ca.gov/announcements/
- group: start
  title: ''
  type: DataBrokerRegistryData
  url: https://cppa.ca.gov/data_broker_registry/complete-reg-data-brokers.csv
created: '2025-01-01'
description: 'The California Consumer Privacy Act (CCPA), amended by the California Privacy Rights Act (CPRA), is a state statute that grants California residents rights over their personal information: the right to know, delete, correct, opt-out of sale/sharing, limit use of sensitive personal information, and non-discrimination for exercising privacy rights. It is enforced by the California Privacy Protection Agency (CPPA) and the California Attorney General. Technical interoperability mechanisms include the Global Privacy Control (GPC) browser signal and the IAB Tech Lab US Privacy (USP) / Global Privacy Platform (GPP) signals for advertising technology. This index tracks the official regulatory resources, technical privacy signals, and commercial APIs that help businesses comply with CCPA/CPRA obligations.'
features:
- name: Notice at Collection
- name: Privacy Policy Disclosure
- name: Do Not Sell or Share Link
- name: Limit Use of Sensitive PI Link
- name: Verifiable Consumer Requests
- name: Authorized Agent Requests
- name: Opt-Out Preference Signal (GPC)
- name: Service Provider / Contractor Contracts
- name: Data Processing Addendum
- name: Data Retention Disclosure
- name: Risk Assessments (CPRA)
- name: Cybersecurity Audits (CPRA)
- name: Automated Decision-Making Disclosures (CPRA)
finops:
- name: Ccpa Finops
  service_category: API
  slug: ccpa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ccpa.png
layout: provider
modified: '2026-09-05'
name: CCPA (California Consumer Privacy Act)
nav: Providers
network: true
overview: 'CCPA (California Consumer Privacy Act) publishes 1 API on the [APIs.io](https://apis.io/) network: CalPrivacy DROP Data Broker API. Tagged areas include CPRA, California, Compliance, Data Protection, and Data Subject Rights.


  The CCPA (California Consumer Privacy Act) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CCPA (California Consumer Privacy Act)''s developer surface includes documentation, FAQ, authentication, changelog, sandbox, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Ccpa Plans Pricing
  plan_count: 2
  slug: ccpa-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Ccpa Rate Limits
  slug: ccpa-rate-limits
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 46.0
    catalog_earned_first_party: 8.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 43.9
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 66.4
    developer_ergonomics: 73.2
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 15.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ccpa/refs/heads/main/screenshots/ccpa-2026-06-20T174058.png
security:
- kind: authentication
  name: Ccpa Authentication
  slug: ccpa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ccpa Domain Security
  slug: ccpa-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ccpa Vulnerability Disclosure
  slug: ccpa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ccpa
tags:
- CPRA
- California
- Compliance
- Data Protection
- Data Subject Rights
- Legal
- Privacy
- Regulations
use_cases:
- name: DSAR (Data Subject Access Request) Automation
- name: Consent Management Platform (CMP)
- name: Cookie Banner and Preference Center
- name: Data Inventory and Mapping
- name: Vendor Risk Management
- name: Privacy Impact Assessments
- name: Audit and Reporting
- name: Global Privacy Control Handling
- name: Data Broker Registration
website: https://oag.ca.gov/privacy/ccpa
---
