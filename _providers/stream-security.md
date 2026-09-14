---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 2
apis:
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: REST API over the Stream Security CloudTwin. 34 operations across twelve resource groups - inventory, attack paths, config changes, threat detections, detection rules, posture security rules and viola
  name: Stream Security API
  slug: stream-security-api
- description: Hosted remote MCP server that lets an agent query the Stream Security CloudTwin in natural language - resource metadata, configuration changes, misconfigurations, external exposures, excessive privile
  name: Stream Security MCP Server
  slug: stream-security-mcp-server
artifact_total: 8
asyncapis:
- description: ''
  name: Stream Security Notifications Webhooks
  slug: stream-security-notifications-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stream-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stream.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.streamsec.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streamsec.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.streamsec.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.streamsec.io/docs/onboarding
- group: company
  title: ''
  type: Blog
  url: https://www.stream.security/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightlytics
- group: start
  title: ''
  type: SignUp
  url: https://app.streamsec.io/
- group: operate
  title: ''
  type: Support
  url: https://www.stream.security/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stream.security/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stream.security/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stream-security-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/stream-security-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stream-security-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/stream-security-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stream-security-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stream-security-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stream-security-authentication.yml
created: '2026-08-29'
description: Stream.Security (formerly Lightlytics) is a cloud detection and response (CDR) and real-time CNAPP vendor that builds a live model of a customer's cloud - its "CloudTwin" - by continuously ingesting configuration state and activity from AWS, Azure, GCP, Kubernetes, ECS and VMware vSphere, then correlating posture drift against runtime behaviour to expose exploitable attack paths, excessive privilege, external exposure and active threats. The platform combines cloud-native log ingestion (CloudTrail, VPC Flow Logs, Route53 DNS, ELB/ALB, WAF, Entra ID audit) with eBPF runtime agents on Kubernetes, ECS and standalone VMs, adds canary/trap decoy resources and auto-remediation, and exposes it all through a public REST API and an MCP server so security teams and agents can query inventory, detections, vulnerabilities, attack paths and posture violations programmatically.
image: https://cdn.prod.website-files.com/5f05d585ae7f3b0c47bc77a4/67166fa0d1d0600f5c5d67e8_page-preview.png
layout: provider
mcp_servers:
- description: Lets an agent interact with Stream Security data in natural language - retrieving resource metadata, configuration changes, misconfigurations, external exposures, excessive privileges and access to cr
  name: Stream Security MCP Server
  slug: stream-security-mcp-server
modified: '2026-08-29'
name: Stream.Security
nav: Providers
network: true
overview: 'Stream.Security publishes 1 API on the [APIs.io](https://apis.io/) network: Stream Security API. Tagged areas include Company, Security, Cloud Security, Cloud Detection and Response, and CNAPP.


  The Stream.Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Stream.Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 13 more developer resources.'
plans:
- name: Stream Security Plans Pricing
  plan_count: 0
  slug: stream-security-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Stream Security Rate Limits
  slug: stream-security-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/stream-security/refs/heads/main/screenshots/stream-security-2026-09-02T161000.png
security:
- kind: authentication
  name: Stream Security Authentication
  slug: stream-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stream Security Domain Security
  slug: stream-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stream-security
tags:
- Company
- Security
- Cloud Security
- Cloud Detection and Response
- CNAPP
- Threat Detection
- Vulnerability Management
- Kubernetes
- Observability
- DevSecOps
- Artificial Intelligence
website: https://www.stream.security/
---
