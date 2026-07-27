---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'The Australian Energy Regulator (AER) is the independent national economic regulator of Australia''s energy markets, established under the Competition and Consumer Act 2010 and operating alongside the ACCC. It sets network revenues and prices, enforces the National Electricity, Gas and Energy Retail Rules, monitors wholesale and retail market conduct, sets the Default Market Offer, keeps the public registers of authorised retailers and exemptions, and operates Energy Made Easy, the government price-comparison service. Its API posture is the strongest found among Australian energy regulators and it is genuinely implemented rather than merely mandated. The AER is a designated data holder under the Competition and Consumer (Consumer Data Right) Rules 2020 and it serves the Consumer Data Standards energy Product Reference Data endpoints — Get Generic Plans and Get Generic Plan Detail — anonymously, with no accreditation, no API key and no signup, returning live retail plan, tariff,
  fee, discount and eligibility data for the six jurisdictions that adopted the National Energy Customer Framework. Verified on 2026-07-27, 79 of the 84 energy data-holder brands in the ACCC CDR Register point their productBaseUri at the AER''s own host, cdr.energymadeeasy.gov.au, which makes the regulator the actual operator of the product-data API layer for nearly the whole Australian retail energy industry. The split matters: the AER''s open surface is product and tariff data only. It holds and exposes no individual consumer usage or billing data — the CDR consumer endpoints 404 on its host — because those flow from retailers as primary data holders and AEMO as the secondary data holder gateway, behind ACCC accreditation, OAuth2/OIDC and mTLS. The AER''s own market statistics, wholesale performance reporting and public registers are published as web pages, charts and document downloads, not as an API, and no developer., developers., api., docs. or data. subdomain resolves.'
image: https://www.aer.gov.au/sites/default/files/2023-08/logo-2x.png
layout: provider
modified: '2026-07-27'
name: Australian Energy Regulator
nav: Providers
network: true
random_paper: 40
slug: aer
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Markets
- Consumer Data Right
- Retail Energy
- Regulation
- Government
- Open Data
- Smart Metering
---
