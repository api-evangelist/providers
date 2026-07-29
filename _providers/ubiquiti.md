---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ubiquiti Agentic Access
  operation_count: 9
  slug: ubiquiti-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 8
apis:
- description: 'The UniFi Network Controller API is the local HTTP API exposed by every UniFi Network controller (UDM, UDM Pro, UDR, Cloud Key, self-hosted controller, UniFi OS consoles). Endpoints are prefixed with '
  name: UniFi Network Controller API
  slug: unifi-network-controller-api
- description: The UISP Network (NMS) API is the per-instance REST API for the network-management half of UISP — Ubiquiti's purpose-built ISP platform for wireless and fiber service providers. Endpoints are served f
  name: UISP Network (NMS) API
  slug: uisp-nms-api
- description: The UISP CRM API is the per-instance REST API for the customer-relationship-management half of UISP, covering clients, services (subscriptions), invoices, payments, quotes, tickets, jobs, taxes, and p
  name: UISP CRM API
  slug: uisp-crm-api
- description: UniFi devices managed by the account's hosts
  name: Ubiquiti Devices API
  slug: ubiquiti-devices-api
- description: UniFi OS consoles linked to the UI account
  name: Ubiquiti Hosts API
  slug: ubiquiti-hosts-api
- description: WAN performance metrics (latency, packet loss, uptime, bandwidth)
  name: Ubiquiti ISP Metrics API
  slug: ubiquiti-isp-metrics-api
- description: SD-WAN configurations and deployment status
  name: Ubiquiti SD-WAN API
  slug: ubiquiti-sd-wan-api
- description: UniFi Network application sites
  name: Ubiquiti Sites API
  slug: ubiquiti-sites-api
artifact_total: 27
collections:
- collection_type: open
  name: UniFi Site Manager API
  slug: open-ubiquiti-unifi-site-manager-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ubiquiti-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ubiquiti-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubiquiti-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubiquiti-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.ui.com
- group: start
  title: ''
  type: Portal
  url: https://developer.ui.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ui.com/site-manager-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ui.com/hc/en-us/articles/30076656117655-Getting-Started-with-the-Official-UniFi-API
- group: docs
  title: ''
  type: Documentation
  url: https://ubntwiki.com/products/software/unifi-controller/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.uisp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://unmscrm.docs.apiary.io/
- group: start
  title: ''
  type: Portal
  url: https://amplifi.com
- group: start
  title: ''
  type: Signup
  url: https://account.ui.com
- group: auth
  title: ''
  type: Authentication
  url: https://unifi.ui.com/settings/api-keys
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.ui.com/site-manager-api/
- group: design
  title: ''
  type: Versioning
  url: https://developer.ui.com/site-manager-api/versioncontrol
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ui.com
- group: company
  title: ''
  type: Blog
  url: https://www.ui.com/blog
- group: operate
  title: ''
  type: Forums
  url: https://community.ui.com
- group: operate
  title: ''
  type: Support
  url: https://help.ui.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ui.com/legal/termsofservice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ui.com/legal/privacypolicy/
- group: company
  title: ''
  type: Investors
  url: https://ir.ui.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubiquiti
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubiquiti-community
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Art-of-WiFi/UniFi-API-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ubiquiti-community/go-unifi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ubiquiti-community/py-unifi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DiegoMax/uisp
- group: build
  title: ''
  type: Tools
  url: https://github.com/ubiquiti-community/terraform-provider-unifi
- group: build
  title: ''
  type: Tools
  url: https://github.com/ubiquiti-community/external-dns-unifi-webhook
- group: commercial
  title: ''
  type: Plans
  url: plans/ubiquiti-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ubiquiti-rate-limits.yml
created: '2026-05-25T00:00:00.000Z'
description: Ubiquiti Inc. (NYSE&#58; UI) is an American networking technology company that designs and sells wireless and wired network products for enterprises, service providers, and consumers under the UniFi, UISP, AmpliFi, airMAX, airFiber, and EdgeMax brands. UniFi is a full-stack platform spanning WiFi, switching, routing, identity, surveillance (Protect), access control (Access), and VoIP (Talk), managed locally by the UniFi Network Controller and globally via the UniFi Site Manager cloud at unifi.ui.com. UISP is Ubiquiti's ISP platform combining a Network Management System (NMS) and a Customer Relationship Management (CRM) module for wireless and fiber service providers. The official UniFi Site Manager API exposes hosts, sites, devices, ISP metrics, and SD-WAN configurations at api.ui.com/v1 with X-API-KEY authentication; UISP NMS and CRM APIs are hosted on each customer instance under /nms/api/v2.1/ and /crm/api/v1.0/ respectively.
features:
- UniFi — full-stack networking with WiFi access points (UniFi 7), switches, routers (Dream Machine, Dream Router, Dream Wall), VPN, identity, protect cameras, access control, and talk VoIP
- UniFi Site Manager — cloud-based multi-site management at unifi.ui.com with an official REST API at api.ui.com/v1
- UniFi Network Controller — on-premises controller (UDM/UDR/Cloud Key/self-host) with a local REST API used by mobile apps and the web console
- UISP — purpose-built management platform for wireless ISPs and fiber operators, combining NMS (devices, sites, outages) and CRM (clients, invoices, payments)
- AmpliFi — consumer mesh WiFi line with Teleport VPN; managed via mobile app (no public API)
- airMAX / airFiber / GigaBeam / LTU — point-to-point and point-to-multipoint outdoor radios for ISPs
- UniFi Protect — camera and NVR ecosystem with motion analytics and AI detection
- UniFi Access — door access control with NFC, mobile credentials, and visitor management
- UniFi Talk — cloud-hosted VoIP for SMB
- WiFiman speed-test and discovery tools, plus the WiFiman developer SDK
- Official Postman / curl quickstarts and rate-limit headers on the Site Manager API
- Read-only API keys at GA; write scope (adopt, configure) rolling out through 2026
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ubiquiti.png
layout: provider
modified: '2026-05-25'
name: Ubiquiti
nav: Providers
network: true
overview: 'Ubiquiti publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Hosts API, ISP Metrics API, and 2 more. Tagged areas include Networking, WiFi, Switching, Routing, and Surveillance.


  Ubiquiti''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, engineering blog, support, and 26 more developer resources.'
plans:
- name: Ubiquiti Plans Pricing
  plan_count: 3
  slug: ubiquiti-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Ubiquiti Rate Limits
  slug: ubiquiti-rate-limits
score:
  band: developing
  composite: 53.5
  delta: -1.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.9
    developer_ergonomics: 60.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubiquiti/refs/heads/main/screenshots/ubiquiti-2026-06-20T195930.png
security:
- kind: authentication
  name: Ubiquiti Authentication
  slug: ubiquiti-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ubiquiti Domain Security
  slug: ubiquiti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ubiquiti Vulnerability Disclosure
  slug: ubiquiti-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ubiquiti
tags:
- Networking
- WiFi
- Switching
- Routing
- Surveillance
- Access Control
- ISP
- WISP
- UniFi
- UISP
- AmpliFi
website: https://www.ui.com
---
