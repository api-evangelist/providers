---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Gcore Agentic Access
  operation_count: 31
  slug: gcore-agentic-access
  summary_line: 31 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Content delivery network resources, rules, origin groups, and purge.
  name: Gcore CDN API
  slug: gcore-cdn-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Virtual machine instances, networks, and volumes.
  name: Gcore Cloud API
  slug: gcore-cloud-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Managed authoritative DNS zones and RRSets.
  name: Gcore DNS API
  slug: gcore-dns-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Serverless edge functions and applications.
  name: Gcore FastEdge API
  slug: gcore-fastedge-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Everywhere Inference edge AI model deployments.
  name: Gcore Inference API
  slug: gcore-inference-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: S3-compatible and SFTP object storage.
  name: Gcore Storage API
  slug: gcore-storage-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Video hosting (VOD) and live streaming.
  name: Gcore Streaming API
  slug: gcore-streaming-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Web Application and API Protection domains.
  name: Gcore WAAP API
  slug: gcore-waap-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gcore CDN API
  slug: open-gcore-cdn-api
- collection_type: open
  name: Gcore CDN Cloud API
  slug: open-gcore-cloud-api
- collection_type: open
  name: Gcore CDN DNS API
  slug: open-gcore-dns-api
- collection_type: open
  name: Gcore CDN FastEdge API
  slug: open-gcore-fastedge-api
- collection_type: open
  name: Gcore CDN Inference API
  slug: open-gcore-inference-api
- collection_type: open
  name: Gcore CDN Storage API
  slug: open-gcore-storage-api
- collection_type: open
  name: Gcore CDN Streaming API
  slug: open-gcore-streaming-api
- collection_type: open
  name: Gcore CDN WAAP API
  slug: open-gcore-waap-api
- collection_type: open
  name: Gcore API
  slug: open-gcore
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gcore-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gcore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gcore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gcore-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/G-Core
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gcore
- group: company
  title: ''
  type: Website
  url: https://gcore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gcore.com/docs/api-reference/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/gcore-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gcore-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gcore-finops.yml
created: '2026-06-20'
description: Gcore is a global edge cloud, CDN, streaming, and AI infrastructure provider operating 210+ points of presence. A single REST platform at https://api.gcore.com (APIKey auth) spans content delivery, GPU cloud and bare-metal compute, S3-compatible object storage, managed DNS, video streaming and live, Everywhere Inference (edge AI), WAAP/DDoS security, and FastEdge serverless functions.
finops:
- name: Gcore Finops
  service_category: Compute and Networking
  slug: gcore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gcore.png
layout: provider
modified: '2026-06-20'
name: Gcore
nav: Providers
network: true
overview: 'Gcore publishes 8 APIs on the [APIs.io](https://apis.io/) network, including CDN API, Cloud API, DNS API, and 5 more. Tagged areas include Edge Cloud, CDN, Streaming, Edge AI, and Infrastructure.


  Gcore''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Gcore Plans Pricing
  plan_count: 8
  slug: gcore-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Gcore Rate Limits
  slug: gcore-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/gcore/refs/heads/main/screenshots/gcore-2026-06-20T181710.png
security:
- kind: authentication
  name: Gcore Authentication
  slug: gcore-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gcore Domain Security
  slug: gcore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gcore
tags:
- Edge Cloud
- CDN
- Streaming
- Edge AI
- Infrastructure
website: https://gcore.com/
---
