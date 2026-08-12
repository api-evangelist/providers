---
api_count: 1
artifact_total: 0
coverage:
  checked: '2026-08-11'
  detail: CyberCube's Atlas documentation portal ships a SwaggerUI/apidom OpenAPI renderer in its JS bundle but serves every anonymous request the same 2,259-byte login shell, and the production API host api.cybcube.com answers unauthenticated calls with an AWS API Gateway MissingAuthenticationTokenException — the specification exists, only its distribution is closed.
  evidence:
  - status: 403
    url: https://api.cybcube.com/openapi.json
  - status: 200
    url: https://docs.atlas.cybcube.com/openapi.json
  - status: 403
    url: https://api.docs.atlas.cybcube.com/
  - status: 404
    url: https://www.cybcube.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-11'
description: CyberCube is a cyber risk analytics provider for the insurance industry — brokers, insurers, reinsurers and cyber ILS investors — translating cyber risk into quantified financial impact. Its product line spans Account Manager (single-risk underwriting), Portfolio Manager (portfolio aggregation and catastrophe loss modeling), Broking Manager, Exposure Manager, SPoF Intelligence (digital supply-chain single points of failure) and the Industry Exposure Databases. CyberConnect is the company's API layer, marketed as a way to deliver CyberCube models, insights and signals into a customer's own underwriting, exposure-management and capital-modeling workflows, spanning catastrophe risk management, risk scoring, financial loss modeling, reinsurance modeling, SPoF intelligence, risk intelligence and threat modeling. The CyberConnect reference and the Atlas documentation portal sit behind a customer login, and the production API host answers unauthenticated requests with an AWS API Gateway
  authentication challenge.
image: https://www.cybcube.com/hubfs/cybercube-logo-white.svg
layout: provider
modified: '2026-08-11'
name: CyberCube
nav: Providers
network: true
random_paper: 20
slug: cybercube
tags:
- Company
- Cyber Risk
- Insurance
- Analytics
- Risk Modeling
- Cybersecurity
- Reinsurance
- Catastrophe Modeling
- Underwriting
- InsurTech
---
