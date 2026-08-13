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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 4
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
artifact_total: 31
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
- group: other
  title: ''
  type: Enforcement
  url: https://cppa.ca.gov/enforcement/
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
modified: '2026-04-23'
name: CCPA (California Consumer Privacy Act)
nav: Providers
network: true
overview: 'CCPA (California Consumer Privacy Act) publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CPRA, California, Compliance, Data Protection, and Data Subject Rights.


  CCPA (California Consumer Privacy Act)''s developer surface includes documentation, FAQ, and 10 more developer resources.'
plans:
- name: Ccpa Plans Pricing
  plan_count: 3
  slug: ccpa-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Ccpa Rate Limits
  slug: ccpa-rate-limits
score:
  band: minimal
  composite: 12.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ccpa/refs/heads/main/screenshots/ccpa-2026-06-20T174058.png
security:
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
- Regulation
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
