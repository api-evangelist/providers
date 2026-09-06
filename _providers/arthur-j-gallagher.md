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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Arthur J Gallagher Agentic Access
  operation_count: 4
  slug: arthur-j-gallagher-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: API for integrating with Gallagher Bassett claims management services. Gallagher Bassett is a global third-party claims administrator and subsidiary of Arthur J. Gallagher, providing workers compensat
  name: Gallagher Bassett Claims Management API
  slug: gallagher-bassett-api
- baseURL: https://localhost:8904/api
  baseurl_source: declared
  description: Manage access control groups.
  name: Arthur J. Gallagher Access Groups API
  slug: arthur-j-gallagher-access-groups-api
- baseURL: https://localhost:8904/api
  baseurl_source: declared
  description: Monitor and manage security alarms.
  name: Arthur J. Gallagher Alarms API
  slug: arthur-j-gallagher-alarms-api
- baseURL: https://localhost:8904/api
  baseurl_source: declared
  description: Manage cardholders in the security system.
  name: Arthur J. Gallagher Cardholders API
  slug: arthur-j-gallagher-cardholders-api
- baseURL: https://localhost:8904/api
  baseurl_source: declared
  description: Retrieve security events and audit logs.
  name: Arthur J. Gallagher Events API
  slug: arthur-j-gallagher-events-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gallagher Command Centre REST Access Groups API
  slug: open-arthur-j-gallagher-access-groups-api
- collection_type: open
  name: Gallagher Command Centre REST Access Groups Alarms API
  slug: open-arthur-j-gallagher-alarms-api
- collection_type: open
  name: Gallagher Command Centre REST Access Groups Cardholders API
  slug: open-arthur-j-gallagher-cardholders-api
- collection_type: open
  name: Gallagher Command Centre REST Access Groups Events API
  slug: open-arthur-j-gallagher-events-api
- collection_type: open
  name: Gallagher Command Centre REST API
  slug: open-gallagher-command-centre-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/arthur-j-gallagher-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arthur-j-gallagher-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arthur-j-gallagher-domain-security.yml
- group: start
  title: Arthur J. Gallagher Website
  type: Portal
  url: https://www.ajg.com/
- group: docs
  title: Gallagher Security Developer Docs
  type: Documentation
  url: https://gallaghersecurity.github.io/
- group: start
  title: Gallagher Bassett Developer Portal
  type: Portal
  url: https://developer.gallagherbassett.com/
- group: build
  title: Gallagher Security GitHub
  type: GitHubOrganization
  url: https://github.com/GallagherSecurity
created: '2025-03-01'
description: Arthur J. Gallagher & Co. is a global insurance brokerage, risk management, and consulting firm headquartered in Rolling Meadows, Illinois. The company provides insurance brokerage, risk management, employee benefits, and retirement services to clients worldwide. Its subsidiaries include Gallagher Security (which offers the Command Centre REST API for physical security integration) and Gallagher Bassett (which offers claims management APIs for third-party claims administration). Arthur J. Gallagher serves clients in over 130 countries through its international network of brokers and offices.
features:
- description: Full REST API for integrating with Gallagher's Command Centre physical security system, enabling access control, alarm management, visitor tracking, and event monitoring from third-party applications.
  name: Command Centre REST API
- description: Internet-based secure connectivity to Command Centre servers, enabling remote integration without VPN through the Gallagher Cloud API Gateway.
  name: Cloud API Gateway
- description: SDK for developing mobile applications that connect to Gallagher Command Centre for access control, including code samples and technical guides.
  name: Mobile Connect SDK
- description: Gallagher Bassett API for programmatic integration with third-party claims administration workflows including claim submission, status tracking, and reporting.
  name: Claims Management API
finops:
- name: Arthur J Gallagher Finops
  service_category: API
  slug: arthur-j-gallagher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arthur-j-gallagher.png
integrations:
- description: Formal partner program for companies integrating with Command Centre, providing access to proprietary technology resources, software licenses, and technical support.
  name: Gallagher Security Technology Partner Program
- description: Third-party administrators and enterprise clients integrate with Gallagher Bassett for outsourced claims management workflows.
  name: Gallagher Bassett Claims Administration
layout: provider
modified: '2026-05-19'
name: Arthur J. Gallagher
nav: Providers
network: true
overview: 'Arthur J. Gallagher publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Access Groups API, Alarms API, Cardholders API, and 1 more. Tagged areas include Insurance, Brokerage, Risk Management, Claims Management, and Security.


  Arthur J. Gallagher''s developer surface includes developer portal, documentation, and 5 more developer resources.'
plans:
- name: Arthur J Gallagher Plans Pricing
  plan_count: 3
  slug: arthur-j-gallagher-plans-pricing
press:
- date: '2026-05-25'
  title: 'Arthur J Gallagher''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/arthur-j-gallagher-ai-strategy-analysis-of-dominance-in-insurance-ai/
- date: '2026-05-25'
  title: 'Gallagher AI survey: 82% of respondents report positive ...'
  url: https://investor.ajg.com/news/news-details/2026/Gallagher-AI-survey-82-of-respondents-report-positive-impacts-though-data-protection-errors-remain-top-challenges/default.aspx
- date: '2026-05-25'
  title: Arthur J Gallagher earnings on deck as AI worries meet ...
  url: https://www.investing.com/news/earnings/arthur-j-gallagher-earnings-on-deck-as-ai-worries-meet-revenue-growth-93CH-4650464
- date: '2026-05-25'
  title: Gallagher launches Blueprint AI risk scoring framework
  url: https://www.stocktitan.net/news/AJG/gallagher-launches-gallagher-blueprint-pairing-ai-and-expert-insight-rikhjs4fhwpo.html
- date: ''
  title: Two-thirds of organizations invest in AI training as adoption ...
  url: https://www.prnewswire.com/news-releases/two-thirds-of-organizations-invest-in-ai-training-as-adoption-accelerates
random_paper: 8
rate_limits:
- limit_count: 5
  name: Arthur J Gallagher Rate Limits
  slug: arthur-j-gallagher-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arthur-j-gallagher/refs/heads/main/screenshots/arthur-j-gallagher-2026-06-20T172441.png
security:
- kind: domain-security
  name: Arthur J Gallagher Domain Security
  slug: arthur-j-gallagher-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arthur-j-gallagher
tags:
- Insurance
- Brokerage
- Risk Management
- Claims Management
- Security
- Benefits
- Fortune 1000
use_cases:
- description: Technology partners integrate Command Centre REST API to build visitor management systems, CCTV integrations, and security operations center dashboards.
  name: Physical Security Integration
- description: Corporate IT teams integrate access control with HR systems to automatically provision and deprovision employee badge access based on employment status changes.
  name: Access Control Automation
- description: Enterprise clients integrate Gallagher Bassett's claims API with their ERP and HR systems to automate workers compensation and liability claims submission and tracking.
  name: Claims Processing Integration
- description: Security operations teams use the Command Centre API to correlate access events with alarm triggers for automated incident response and reporting.
  name: Incident Response
website: https://www.ajg.com/
---
