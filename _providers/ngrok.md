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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 79
  human_in_the_loop: 1
  name: Ngrok Agentic Access
  operation_count: 134
  slug: ngrok-agentic-access
  summary_line: 134 operations · 79 acting · 1 human-in-the-loop
api_count: 24
apis:
- description: Abuse Reports allow you to submit reports of abusive endpoints.
  name: ngrok Abuse Reports API
  slug: ngrok-abuse-reports-api
- description: Agent Ingresses are the addresses ngrok agents connect to.
  name: ngrok Agent Ingresses API
  slug: ngrok-agent-ingresses-api
- description: API Keys are used to authenticate to the ngrok API.
  name: ngrok API Keys API
  slug: ngrok-api-keys-api
- description: Backends define how traffic is handled, including tunnel group, weighted, failover, HTTP response, and static address backends.
  name: ngrok Backends API
  slug: ngrok-backends-api
- description: Certificate Authorities are x509 certificates used for mutual TLS authentication.
  name: ngrok Certificate Authorities API
  slug: ngrok-certificate-authorities-api
- description: Tunnel Credentials are authtokens used to start ngrok tunnels.
  name: ngrok Credentials API
  slug: ngrok-credentials-api
- description: HTTPS Edges define HTTPS endpoints with routes and modules.
  name: ngrok Edges HTTPS API
  slug: ngrok-edges-https-api
- description: TCP Edges define TCP endpoints for non-HTTP protocols.
  name: ngrok Edges TCP API
  slug: ngrok-edges-tcp-api
- description: TLS Edges define TLS endpoints with TLS termination and mutual TLS.
  name: ngrok Edges TLS API
  slug: ngrok-edges-tls-api
- description: Endpoints represent the public URLs of active tunnels and edges.
  name: ngrok Endpoints API
  slug: ngrok-endpoints-api
- description: Event Destinations define where event data is sent.
  name: ngrok Event Destinations API
  slug: ngrok-event-destinations-api
- description: Event Subscriptions define which events trigger notifications.
  name: ngrok Event Subscriptions API
  slug: ngrok-event-subscriptions-api
- description: IP Policies contain rules to allow or deny traffic from IP ranges.
  name: ngrok IP Policies API
  slug: ngrok-ip-policies-api
- description: IP Policy Rules are CIDR-based allow/deny rules within an IP Policy.
  name: ngrok IP Policy Rules API
  slug: ngrok-ip-policy-rules-api
- description: IP Restrictions apply IP Policies to specific ngrok resources.
  name: ngrok IP Restrictions API
  slug: ngrok-ip-restrictions-api
- description: Reserved Addresses are static TCP addresses for TCP tunnels.
  name: ngrok Reserved Addresses API
  slug: ngrok-reserved-addresses-api
- description: Reserved Domains are custom hostnames for HTTP/HTTPS/TLS tunnels.
  name: ngrok Reserved Domains API
  slug: ngrok-reserved-domains-api
- description: SSH Certificate Authorities manage keys for signing SSH certificates.
  name: ngrok SSH Certificate Authorities API
  slug: ngrok-ssh-certificate-authorities-api
- description: SSH Credentials are public keys for authenticating SSH tunnel sessions.
  name: ngrok SSH Credentials API
  slug: ngrok-ssh-credentials-api
- description: SSH Host Certificates authenticate ngrok tunnel servers to clients.
  name: ngrok SSH Host Certificates API
  slug: ngrok-ssh-host-certificates-api
- description: SSH User Certificates authenticate users to ngrok SSH tunnel servers.
  name: ngrok SSH User Certificates API
  slug: ngrok-ssh-user-certificates-api
- description: TLS Certificates are x509 certificate/key pairs used to terminate TLS traffic.
  name: ngrok TLS Certificates API
  slug: ngrok-tls-certificates-api
- description: Tunnel Sessions represent running ngrok agent connections.
  name: ngrok Tunnel Sessions API
  slug: ngrok-tunnel-sessions-api
- description: Tunnels represent individual tunnels within a tunnel session.
  name: ngrok Tunnels API
  slug: ngrok-tunnels-api
artifact_total: 72
collections:
- collection_type: postman
  name: Ngrok Abuse Reports API
  slug: postman-ngrok-abuse-reports-api
- collection_type: postman
  name: Ngrok Abuse Reports Agent Ingresses API
  slug: postman-ngrok-agent-ingresses-api
- collection_type: postman
  name: Ngrok Abuse Reports API Keys API
  slug: postman-ngrok-api-keys-api
- collection_type: postman
  name: Ngrok Abuse Reports Backends API
  slug: postman-ngrok-backends-api
- collection_type: postman
  name: Ngrok Abuse Reports Certificate Authorities API
  slug: postman-ngrok-certificate-authorities-api
- collection_type: postman
  name: Ngrok Abuse Reports Credentials API
  slug: postman-ngrok-credentials-api
- collection_type: postman
  name: Ngrok Abuse Reports Edges HTTPS API
  slug: postman-ngrok-edges-https-api
- collection_type: postman
  name: Ngrok Abuse Reports Edges TCP API
  slug: postman-ngrok-edges-tcp-api
- collection_type: postman
  name: Ngrok Abuse Reports Edges TLS API
  slug: postman-ngrok-edges-tls-api
- collection_type: postman
  name: Ngrok Abuse Reports Endpoints API
  slug: postman-ngrok-endpoints-api
- collection_type: postman
  name: Ngrok Abuse Reports Event Destinations API
  slug: postman-ngrok-event-destinations-api
- collection_type: postman
  name: Ngrok Abuse Reports Event Subscriptions API
  slug: postman-ngrok-event-subscriptions-api
- collection_type: postman
  name: Ngrok Abuse Reports IP Policies API
  slug: postman-ngrok-ip-policies-api
- collection_type: postman
  name: Ngrok Abuse Reports IP Policy Rules API
  slug: postman-ngrok-ip-policy-rules-api
- collection_type: postman
  name: Ngrok Abuse Reports IP Restrictions API
  slug: postman-ngrok-ip-restrictions-api
- collection_type: postman
  name: Ngrok Abuse Reports Reserved Addresses API
  slug: postman-ngrok-reserved-addresses-api
- collection_type: postman
  name: Ngrok Abuse Reports Reserved Domains API
  slug: postman-ngrok-reserved-domains-api
- collection_type: postman
  name: Ngrok Abuse Reports SSH Certificate Authorities API
  slug: postman-ngrok-ssh-certificate-authorities-api
- collection_type: postman
  name: Ngrok Abuse Reports SSH Credentials API
  slug: postman-ngrok-ssh-credentials-api
- collection_type: postman
  name: Ngrok Abuse Reports SSH Host Certificates API
  slug: postman-ngrok-ssh-host-certificates-api
- collection_type: postman
  name: Ngrok Abuse Reports SSH User Certificates API
  slug: postman-ngrok-ssh-user-certificates-api
- collection_type: postman
  name: Ngrok Abuse Reports TLS Certificates API
  slug: postman-ngrok-tls-certificates-api
- collection_type: postman
  name: Ngrok Abuse Reports Tunnel Sessions API
  slug: postman-ngrok-tunnel-sessions-api
- collection_type: postman
  name: Ngrok Abuse Reports Tunnels API
  slug: postman-ngrok-tunnels-api
- collection_type: open
  name: Ngrok API
  slug: open-ngrok-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ngrok/ngrok-openapi/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/ngrok/.github/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/ngrok/ngrok-openapi/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ngrok/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ngrok-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ngrok-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ngrok-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ngrok-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ngrok-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ngrok
- group: company
  title: ''
  type: Website
  url: https://ngrok.com
- group: docs
  title: ''
  type: Documentation
  url: https://ngrok.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ngrok.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://ngrok.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://ngrok.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://ngrok.com/docs/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://ngrok.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://ngrok.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ngrok.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ngrok
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/ngrok/ngrok-go
- group: build
  title: Rust SDK
  type: SDKs
  url: https://github.com/ngrok/ngrok-rust
- group: build
  title: JavaScript SDK
  type: SDKs
  url: https://github.com/ngrok/ngrok-javascript
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/ngrok/ngrok-python
- group: other
  title: Terraform Provider
  type: Terraform
  url: https://registry.terraform.io/providers/ngrok/ngrok/latest
- group: other
  title: Kubernetes Operator
  type: KubernetesOperator
  url: https://github.com/ngrok/ngrok-operator
- group: other
  title: ''
  type: X
  url: https://x.com/ngrokHQ
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/ngrok/agent-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://ngrok.com/llms.txt
created: '2025-01-08'
description: ngrok is a unified application delivery network for developers, providing secure tunnels, ingress-as-a-service, API gateway, and AI gateway capabilities. It enables developers to expose local services on the public internet, manage edge ingress, and route traffic to AI providers without redeploying applications. ngrok provides a unique URL for each tunnel, traffic policy controls, and a comprehensive REST API for programmatic management of all resources.
finops:
- name: Ngrok Finops
  service_category: API
  slug: ngrok-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ngrok.png
json_schemas:
- name: ngrok API Key
  property_count: 7
  slug: api-key
- name: ngrok Endpoint
  property_count: 17
  slug: endpoint
- name: ngrok Event Subscription
  property_count: 7
  slug: event-subscription
- name: ngrok HTTPS Edge
  property_count: 7
  slug: https-edge
- name: ngrok IP Policy
  property_count: 5
  slug: ip-policy
- name: ngrok Reserved Address
  property_count: 7
  slug: reserved-addr
- name: ngrok Reserved Domain
  property_count: 12
  slug: reserved-domain
- name: ngrok TCP Edge
  property_count: 8
  slug: tcp-edge
- name: ngrok TLS Certificate
  property_count: 13
  slug: tls-certificate
- name: ngrok TLS Edge
  property_count: 10
  slug: tls-edge
- name: ngrok Tunnel Session
  property_count: 10
  slug: tunnel-session
- name: ngrok Tunnel
  property_count: 12
  slug: tunnel
jsonld:
- class_count: 0
  name: Ngrok Context
  property_count: 12
  slug: ngrok-context
layout: provider
modified: '2026-05-30'
name: ngrok
nav: Providers
network: true
overview: 'ngrok publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Abuse Reports API, Agent Ingresses API, API Keys API, and 21 more. Tagged areas include AI Gateway, API Gateway, Compute, Developer Tools, and Gateways.


  The ngrok catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ngrok''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, changelog, pricing, and 22 more developer resources.'
plans:
- name: Ngrok Plans Pricing
  plan_count: 3
  slug: ngrok-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 5
  name: Ngrok Rate Limits
  slug: ngrok-rate-limits
rules:
- name: ngrok API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ngrok-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.4
  delta: -6.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 73.1
    developer_ergonomics: 69.6
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 65.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ngrok/refs/heads/main/screenshots/ngrok-2026-06-20T190307.png
security:
- kind: authentication
  name: Ngrok Authentication
  slug: ngrok-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ngrok Domain Security
  slug: ngrok-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ngrok Vulnerability Disclosure
  slug: ngrok-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ngrok Trust Center
  slug: ngrok-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 1
skills:
- name: expose-localhost
  slug: expose-localhost
slug: ngrok
tags:
- AI Gateway
- API Gateway
- Compute
- Developer Tools
- Gateways
- Ingress
- Platform
- Proxies
- Servers
- Tunnels
website: https://ngrok.com
---
