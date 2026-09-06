---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: 'Amphenol designs, manufactures, and markets electrical, electronic, and fiber optic connectors, interconnect systems, antennas, sensors, and cables. The corporate host runs no developer programme: no '
  name: Amphenol Website
  slug: website
- description: An undocumented but live and fully anonymous JSON endpoint that backs Amphenol Industrial's own Parts Search page. GET /search?searchTerm=<part> returns {total, rows[]} where each row is one authorise
  name: Amphenol Industrial Parts Direct Search API
  slug: parts-direct-search
- description: A live Model Context Protocol resource served by Amphenol's automotive division, discovered through RFC 8414 authorization-server metadata and RFC 9728 protected-resource metadata at that host's well-
  name: Amphenol Automotive MCP Server
  slug: automotive-mcp
artifact_total: 29
common:
- group: company
  title: ''
  type: Website
  url: https://www.amphenol.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amphenol-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amphenol-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amphenol-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amphenol-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/amphenol-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amphenol-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/amphenol-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amphenol-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amphenol-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amphenol-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amphenol-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amphenol-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amphenol-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amphenol-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amphenol-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amphenol-vocabulary.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmphenolAdvancedSensors
- group: company
  title: ''
  type: Blog
  url: https://amphenol-industrial.com/news/
- group: start
  title: ''
  type: Portal
  url: https://www.amphenol.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amphenol.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amphenol.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.amphenol.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amphenol
created: '2024-01-01'
description: Amphenol is one of the world's largest designers, manufacturers, and marketers of electrical, electronic, and fiber optic connectors, interconnect systems, antennas, sensors, and cables used across military-aerospace, industrial, automotive, information technology, mobile phones, wireless infrastructure, broadband, medical device, and professional audio markets worldwide.
features:
- description: High-performance electrical connectors for military, aerospace, industrial, automotive, and consumer electronics applications including the industry-standard BNC and MIL-DTL-38999 cylindrical connectors.
  name: Electrical Connectors
- description: Fiber optic connectors, cables, and interconnect systems for telecommunications, data center, and military applications through Amphenol Fiber Systems International (AFSI).
  name: Fiber Optic Connectivity
- description: RF connectors and coaxial cables for wireless infrastructure, broadband, and communications equipment operating across a wide frequency range.
  name: Coaxial Cables and RF Connectors
- description: Electronic sensing solutions for industrial, automotive, and medical applications measuring pressure, temperature, position, and other physical parameters.
  name: Sensor Solutions
- description: Antenna systems for wireless infrastructure, mobile devices, automotive, and IoT applications supporting cellular, Wi-Fi, GPS, and other wireless protocols.
  name: Antenna Systems
- description: Mil-spec and high-reliability aerospace connectors through Amphenol Aerospace for aircraft, defense systems, and space applications meeting MIL-DTL-38999 and other military specifications.
  name: Aerospace Connectors
- description: Ruggedized connectors for defense, aviation, rail, energy, entertainment, and space industries through Amphenol Socapex with qualified products for harsh environments.
  name: Defense and Military Connectors
- description: Electrical connectors and interconnect systems for automotive applications including EV powertrains, ADAS, infotainment, and chassis systems.
  name: Automotive Connectors
- description: Specialized connectors for medical devices requiring biocompatibility, sterilizability, and high reliability for patient-critical applications.
  name: Medical Connectors
finops:
- name: Amphenol Finops
  service_category: Electronic Components
  slug: amphenol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amphenol.png
integrations:
- description: Qualified supplier to Boeing, Lockheed Martin, Raytheon, and other defense and aerospace original equipment manufacturers.
  name: Aerospace and Defense OEMs
- description: Tier 1 and Tier 2 supplier to major automotive manufacturers including GM, Ford, Toyota, and EV manufacturers for electrical and electronic connector systems.
  name: Automotive OEM Supply Chain
- description: Connector and antenna supplier to Ericsson, Nokia, Samsung, and other telecom equipment manufacturers for wireless infrastructure.
  name: Telecommunications Equipment Manufacturers
jsonld:
- class_count: 10
  name: Amphenol Context
  property_count: 18
  slug: amphenol-context
layout: provider
mcp_servers:
- description: Amphenol Automotive (amphenol-automotive.com) runs a live, remotely reachable Model Context Protocol server. It was not found in any documentation — it was discovered by probing /.well-known/oauth-aut
  name: Amphenol Automotive MCP Server
  slug: amphenol-automotive-mcp-server
modified: '2026-09-02'
name: Amphenol
nav: Providers
network: true
overview: 'Amphenol publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electronic Connectors, Interconnect Systems, Fiber Optics, Sensors, and Aerospace.


  The Amphenol catalog on APIs.io includes 1 JSON-LD context.


  Amphenol''s developer surface includes authentication, engineering blog, developer portal, support, and 20 more developer resources.'
plans:
- name: Amphenol Plans Pricing
  plan_count: 1
  slug: amphenol-plans-pricing
press:
- date: '2026-05-25'
  title: and cable solutions business from commscope
  url: https://www.sec.gov/Archives/edgar/data/820313/000110465925073344/tm2522435d1_ex99-1.htm
- date: '2026-05-25'
  title: Amphenol Corporation to Acquire Connectivity and Cable ...
  url: https://investors.amphenol.com/news-and-events/news-details/2025/Amphenol-Corporation-to-Acquire-Connectivity-and-Cable-Solutions-Business-From-CommScope/default.aspx
- date: '2026-05-25'
  title: Artificial Intelligence Machine Learning | AI / ML
  url: https://www.amphenol-cs.com/artificial-intelligence
- date: '2026-05-25'
  title: Here's Why Amphenol Stock Popped Today (Hint
  url: https://finance.yahoo.com/news/heres-why-amphenol-stock-popped-173637058.html
- date: '2026-05-25'
  title: Amphenol Corporation Completes Acquisition of OWN and ...
  url: https://investors.amphenol.com/news-and-events/news-details/2025/Amphenol-Corporation-Completes-Acquisition-of-OWN-and-DAS-Businesses-From-CommScope/default.aspx
random_paper: 12
rate_limits:
- limit_count: 0
  name: Amphenol Rate Limits
  slug: amphenol-rate-limits
scopes:
- name: Amphenol Scopes
  scope_count: 0
  slug: amphenol-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 0.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 33.3
    contract_quality: 14.7
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 2.6
  previous_composite: 28.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amphenol/refs/heads/main/screenshots/amphenol-2026-06-20T171939.png
security:
- kind: authentication
  name: Amphenol Authentication
  slug: amphenol-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Amphenol Domain Security
  slug: amphenol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amphenol
tags:
- Electronic Connectors
- Interconnect Systems
- Fiber Optics
- Sensors
- Aerospace
- Automotive
- Defense
- Manufacturing
- Fortune 500
use_cases:
- description: Connect avionics, weapons systems, and defense electronics with mil-spec connectors meeting the most demanding environmental and reliability requirements.
  name: Aerospace and Defense Systems
- description: Enable electric vehicle powertrains, battery management systems, and charging infrastructure with high-voltage and high-current automotive connectors.
  name: Automotive Electrification
- description: Support 5G base station deployment with RF connectors, antennas, and coaxial cables for wireless infrastructure equipment.
  name: 5G Infrastructure
- description: Interconnect servers, switches, and storage with high-speed electrical and fiber optic connectors for data center infrastructure.
  name: Data Center Connectivity
- description: Connect industrial sensors, actuators, and control systems with rugged connectors and cables designed for harsh factory environments.
  name: Industrial Automation
- description: Provide reliable electrical connections for medical imaging, patient monitoring, and surgical equipment requiring biocompatible materials.
  name: Medical Device Integration
website: https://www.amphenol.com/
---
