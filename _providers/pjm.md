---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.1
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: 'PJM''s public wholesale market and system data catalogue, exposed as a REST API behind Azure API Management. Feeds include day-ahead and real-time hourly and five-minute LMPs, ancillary service prices '
  name: PJM Data Miner 2 API
  slug: pjm-data-miner-2-api
- description: The only fully anonymous PJM REST API found on the public surface. It backs the PJM Upcoming Changes page and returns the current planned-outage, delayed-data and impact notices for the whole PJM eToo
  name: PJM Messages Public Web Service
  slug: pjm-messages-public-api
- description: PJM's Open Access Same-Time Information System (OASIS) node, the FERC Order 889 obligation implemented against the NAESB Wholesale Electric Quadrant business practice standards. PJM states support for
  name: PJM OASIS Template API
  slug: pjm-oasis-template-api
- description: The REST authentication front door for every browserless/API integration with PJM eTools. A client POSTs to the PJM single sign-on service with X-OpenAM-Username and X-OpenAM-Password headers and rece
  name: PJM Browserless Authentication API
  slug: pjm-browserless-authentication-api
- description: The browserless REST interface to PJM InSchedule, the eTool market participants use to submit and retrieve bilateral internal energy transaction schedules and contracts. PJM's browserless authenticati
  name: PJM InSchedule Browserless API
  slug: pjm-inschedule-api
- description: The browserless XML-over-HTTP interface to eDART, PJM's Dispatcher Applications and Reporting Tool, used by transmission owners and generation owners to file and query transmission and generator outag
  name: PJM eDART Browserless API
  slug: pjm-edart-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pjm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pjm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pjm.com/
- group: start
  title: ''
  type: APIPortal
  url: https://apiportal.pjm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pjm.com/markets-and-operations/etools
- group: start
  title: ''
  type: SignUp
  url: https://accountmanager.pjm.com/accountmanager/pages/public/new-user.jsf
- group: auth
  title: ''
  type: Authentication
  url: https://www.pjm.com/-/media/DotCom/etools/pjm-browserless-authentication-guide.pdf
- group: auth
  title: ''
  type: Security
  url: https://www.pjm.com/markets-and-operations/etools/security.aspx
- group: company
  title: ''
  type: Blog
  url: https://insidelines.pjm.com/
- group: learn
  title: ''
  type: Learning
  url: https://learn.pjm.com/
- group: operate
  title: ''
  type: Support
  url: https://pjm.my.site.com/publicknowledge/s/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pjm-interconnection
- group: commercial
  title: ''
  type: Legal
  url: https://www.pjm.com/about-pjm/legal
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.pjm.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.pjm.com/-/media/DotCom/etools/data-miner-2/data-miner-2-api-guide.ashx
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pjm.com/-/media/DotCom/etools/data-miner-2/data-miner-2-getting-started-guide.pdf
- group: operate
  title: ''
  type: FAQ
  url: https://learn.pjm.com/three-priorities/keeping-the-lights-on/data-miner-faqs.aspx
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.pjm.com/markets-and-operations/etools/data-miner-2/data-miner-2-release-notes.aspx
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pjm-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pjm.com/markets-and-operations/etools/upcoming-changes
- group: operate
  title: ''
  type: Deprecation
  url: https://www.pjm.com/markets-and-operations/etools/data-miner-2/data-miner-2-release-notes.aspx
- group: operate
  title: ''
  type: Roadmap
  url: https://www.pjm.com/committees-and-groups/forums/tech-change-forum.aspx
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pjm-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pjm-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pjm-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pjm-error-catalog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pjm-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pjm-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/pjm-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/pjm-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pjm-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pjm-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pjm-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pjm-message.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pjm-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pjm-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pjm-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pjm.com/about-pjm/member-services/membership-enrollment
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pjm.com/about-pjm/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pjm.com/-/media/DotCom/about-pjm/privacy-policy-and-notice.pdf
- group: other
  title: ''
  type: Glossary
  url: https://www.pjm.com/glossary
created: '2026-07-27'
description: 'PJM Interconnection is the regional transmission organization (RTO) that operates the largest competitive wholesale electricity market in the United States, coordinating the movement of electricity across all or parts of Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia and the District of Columbia for roughly 67 million people. PJM sits at the wholesale layer of the energy value chain — it has no retail customers, so no Green Button, ESPI or consumer data-sharing obligation applies to it. Its API posture is honestly "rich data, universally gated": PJM publishes a large machine-readable market data catalogue through the Data Miner 2 API at https://api.pjm.com/api/v1 and an Azure API Management developer portal at https://apiportal.pjm.com, but every feed returns HTTP 401 anonymously and a free subscription key is only issued after a PJM Tools account is registered and approved by a Customer
  Account Manager. Its one genuinely mandated interface is the FERC Order 889 / NAESB WEQ OASIS node, which is verifiably live and standards-conformant at https://pjmoasis.pjm.com, though template submission also requires an authenticated PJM SSO session. One genuinely anonymous PJM REST API does exist and is easy to miss: the Messages public web service at https://messages.pjm.com/messages/rest/public/messages, linked as "Web Service" from the Upcoming Changes page, returns the planned-outage and impact notices for the whole PJM tool estate with no credential, in XML or JSON.'
examples:
- key_count: 1
  name: Pjm Messages Public Response
  slug: pjm-messages-public-response
image: https://www.pjm.com/assets/MVC/responsive/img/pjm-logo.png
json_schemas:
- name: PJM Messages Public Web Service response
  property_count: 1
  slug: pjm-message
layout: provider
modified: '2026-07-27'
name: PJM Interconnection
nav: Providers
network: true
overview: 'PJM Interconnection publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Energy Markets, Electricity, and Grid.


  PJM Interconnection''s developer surface includes documentation, signup flow, authentication, engineering blog, support, legal docs, API reference, and 36 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Pjm Rate Limits
  slug: pjm-rate-limits
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 33.3
    contract_quality: 14.7
    developer_ergonomics: 70.8
    discoverability: 74.1
    governance: 33.3
    operational_transparency: 76.3
  previous_composite: 51.0
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 38.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pjm/refs/heads/main/screenshots/pjm-2026-08-17T081252.png
security:
- kind: authentication
  name: Pjm Authentication
  slug: pjm-authentication
  summary_line: apiKey/custom-session-token/mutualTLS/none · 5 schemes
- kind: domain-security
  name: Pjm Domain Security
  slug: pjm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pjm Vulnerability Disclosure
  slug: pjm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pjm
tags:
- Energy
- United States
- Energy Markets
- Electricity
- Grid
- System Operator
- Wholesale Electricity
- Transmission
- Market Data
- Demand Response
website: https://www.pjm.com/
---
