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
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Energy Charts Api Agentic Access
  operation_count: 17
  slug: energy-charts-api-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Import/export values
  name: Energy Charts API import_export API
  slug: energy-charts-api-import-export-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Query power values
  name: Energy Charts API power API
  slug: energy-charts-api-power-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Query price values
  name: Energy Charts API prices API
  slug: energy-charts-api-prices-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Renewable shares
  name: Energy Charts API ren_share API
  slug: energy-charts-api-ren-share-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Energy-Charts import_export API
  slug: open-energy-charts-api-import-export-api
- collection_type: open
  name: Energy-Charts import_export power API
  slug: open-energy-charts-api-power-api
- collection_type: open
  name: Energy-Charts import_export prices API
  slug: open-energy-charts-api-prices-api
- collection_type: open
  name: Energy-Charts import_export ren_share API
  slug: open-energy-charts-api-ren-share-api
- collection_type: open
  name: Energy-Charts API
  slug: open-energy-charts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/energy-charts-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energy-charts-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.energy-charts.info/
- group: other
  title: ''
  type: Provider
  url: https://www.ise.fraunhofer.de/
created: '2025-05-02'
description: The Energy-Charts API, provided by Fraunhofer ISE, delivers European energy data including electricity production by source, day-ahead spot market prices, cross-border electricity trading and physical flows, grid frequency, installed capacity, and renewable energy share forecasts. It covers more than 40 European countries and bidding zones, supports ISO 8601, daily, and UNIX timestamp formats, and is largely licensed under CC BY 4.0.
finops:
- name: Energy Charts Api Finops
  service_category: API
  slug: energy-charts-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-charts-api.png
layout: provider
modified: '2026-05-19'
name: Energy Charts API
nav: Providers
network: true
overview: Energy Charts API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including import_export API, power API, prices API, and 1 more. Tagged areas include Energy, Electricity, Renewables, Grid, and Europe.
plans:
- name: Energy Charts Api Plans Pricing
  plan_count: 3
  slug: energy-charts-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Energy Charts Api Rate Limits
  slug: energy-charts-api-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/energy-charts-api/refs/heads/main/screenshots/energy-charts-api-2026-06-20T180710.png
security:
- kind: domain-security
  name: Energy Charts Api Domain Security
  slug: energy-charts-api-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: energy-charts-api
tags:
- Energy
- Electricity
- Renewables
- Grid
- Europe
- Power
- Pricing
- Forecast
website: https://www.energy-charts.info/
---
