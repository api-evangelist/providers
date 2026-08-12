---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 118
  human_in_the_loop: 1
  name: Netbird Agentic Access
  operation_count: 203
  slug: netbird-agentic-access
  summary_line: 203 operations · 118 acting · 1 human-in-the-loop
api_count: 39
apis:
- description: View information about the accounts.
  name: NetBird Accounts API
  slug: netbird-accounts-api
- description: Manage AWS Marketplace subscriptions.
  name: NetBird AWS Marketplace API
  slug: netbird-aws-marketplace-api
- description: Manage checkout sessions for plan subscriptions.
  name: NetBird Checkout API
  slug: netbird-checkout-api
- description: Interact with and view information about DNS configuration.
  name: NetBird DNS API
  slug: netbird-dns-api
- description: Interact with and view information about custom DNS zones.
  name: NetBird DNS Zones API
  slug: netbird-dns-zones-api
- description: Manage CrowdStrike Falcon EDR integrations.
  name: NetBird EDR Falcon Integrations API
  slug: netbird-edr-falcon-integrations-api
- description: Manage FleetDM EDR integrations.
  name: NetBird EDR FleetDM Integrations API
  slug: netbird-edr-fleetdm-integrations-api
- description: Manage Huntress EDR integrations.
  name: NetBird EDR Huntress Integrations API
  slug: netbird-edr-huntress-integrations-api
- description: Manage Microsoft Intune EDR integrations.
  name: NetBird EDR Intune Integrations API
  slug: netbird-edr-intune-integrations-api
- description: Manage EDR compliance bypass for peers.
  name: NetBird EDR Peers API
  slug: netbird-edr-peers-api
- description: Manage SentinelOne EDR integrations.
  name: NetBird EDR SentinelOne Integrations API
  slug: netbird-edr-sentinelone-integrations-api
- description: Manage event streaming integrations.
  name: NetBird Event Streaming Integrations API
  slug: netbird-event-streaming-integrations-api
- description: View information about the account and network events.
  name: NetBird Events API
  slug: netbird-events-api
- description: The Geo Locations API from NetBird — 2 operation(s) for geo locations.
  name: NetBird Geo Locations API
  slug: netbird-geo-locations-api
- description: Interact with and view information about groups.
  name: NetBird Groups API
  slug: netbird-groups-api
- description: Interact with and view information about identity providers.
  name: NetBird Identity Providers API
  slug: netbird-identity-providers-api
- description: Manage Azure AD identity provider integrations for user and group sync.
  name: NetBird IDP Azure Integrations API
  slug: netbird-idp-azure-integrations-api
- description: Manage Google Workspace identity provider integrations for user and group sync.
  name: NetBird IDP Google Integrations API
  slug: netbird-idp-google-integrations-api
- description: Manage Okta SCIM identity provider integrations for user and group sync.
  name: NetBird IDP Okta SCIM Integrations API
  slug: netbird-idp-okta-scim-integrations-api
- description: Manage generic SCIM identity provider integrations for user and group sync.
  name: NetBird IDP SCIM Integrations API
  slug: netbird-idp-scim-integrations-api
- description: Interact with and view information about the ingress peers and ports.
  name: NetBird Ingress Ports API
  slug: netbird-ingress-ports-api
- description: Instance setup and status endpoints for initial configuration.
  name: NetBird Instance API
  slug: netbird-instance-api
- description: Manage and retrieve account invoices.
  name: NetBird Invoice API
  slug: netbird-invoice-api
- description: Interact with and view information about remote jobs.
  name: NetBird Jobs API
  slug: netbird-jobs-api
- description: MSP portal for Tenant management.
  name: NetBird MSP API
  slug: netbird-msp-api
- description: The Networks API from NetBird — 7 operation(s) for networks.
  name: NetBird Networks API
  slug: netbird-networks-api
- description: Manage notification channels for account event alerts.
  name: NetBird Notifications API
  slug: netbird-notifications-api
- description: Interact with and view information about peers.
  name: NetBird Peers API
  slug: netbird-peers-api
- description: Retrieve available plans and products.
  name: NetBird Plans API
  slug: netbird-plans-api
- description: Interact with and view information about policies.
  name: NetBird Policies API
  slug: netbird-policies-api
- description: Access customer portal for subscription management.
  name: NetBird Portal API
  slug: netbird-portal-api
- description: Interact with and view information about posture checks.
  name: NetBird Posture Checks API
  slug: netbird-posture-checks-api
- description: Interact with and view information about routes.
  name: NetBird Routes API
  slug: netbird-routes-api
- description: Interact with and view information about reverse proxy services.
  name: NetBird Services API
  slug: netbird-services-api
- description: Interact with and view information about setup keys.
  name: NetBird Setup Keys API
  slug: netbird-setup-keys-api
- description: Manage and view information about account subscriptions.
  name: NetBird Subscription API
  slug: netbird-subscription-api
- description: Interact with and view information about tokens.
  name: NetBird Tokens API
  slug: netbird-tokens-api
- description: Retrieve current usage statistics for the account.
  name: NetBird Usage API
  slug: netbird-usage-api
- description: Interact with and view information about users.
  name: NetBird Users API
  slug: netbird-users-api
artifact_total: 46
collections:
- collection_type: open
  name: NetBird REST API
  slug: open-netbird
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netbird-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netbird-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netbird-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netbirdio
- group: company
  title: ''
  type: Website
  url: https://netbird.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netbird.io/
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.netbird.io/api
- group: build
  title: ''
  type: GitHub
  url: https://github.com/netbirdio/netbird
- group: company
  title: ''
  type: Blog
  url: https://netbird.io/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.netbird.io/llms.txt
created: '2025-02-09'
description: NetBird is an Open-Source Zero Trust Networking platform that allows you to create secure private networks for your organization or home. We designed NetBird to be simple and fast, requiring near-zero configuration effort and leaving behind the hassle of opening ports, complex firewall rules, VPN gateways, etc.
finops:
- name: Netbird Finops
  service_category: API
  slug: netbird-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netbird.png
layout: provider
modified: '2026-05-19'
name: NetBird
nav: Providers
network: true
overview: 'NetBird publishes 39 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AWS Marketplace API, Checkout API, and 36 more. Tagged areas include Networking, VPN, Zero Trust, Open Source, and WireGuard.


  NetBird''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 6 more developer resources.'
plans:
- name: Netbird Plans Pricing
  plan_count: 3
  slug: netbird-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Netbird Rate Limits
  slug: netbird-rate-limits
score:
  band: thin
  composite: 32.9
  delta: -7.7
  facets:
    commercial_clarity: 15.8
    contract_quality: 57.0
    developer_ergonomics: 28.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/netbird/refs/heads/main/screenshots/netbird-2026-06-20T190148.png
security:
- kind: authentication
  name: Netbird Authentication
  slug: netbird-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Netbird Domain Security
  slug: netbird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: netbird
tags:
- Networking
- VPN
- Zero Trust
- Open Source
- WireGuard
- Security
website: https://netbird.io/
---
