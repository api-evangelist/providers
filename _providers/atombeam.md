---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: AtomBeam runs a real production API — acg-api.atombeamtech.com, the AWS API Gateway backend of its "Codebook Generator" customer portal, whose Angular bundle names the codebooks/, datasets/, companies/, simulation/, reports/, users/, categories/, notifications/ and tracking/ collections — but it answers 403 Forbidden on every path including /openapi.json, and the guides that would document it live inside a Jira Service Management portal that 302s to a login; the only public technical collateral is a set of Neurpac datasheet PDFs behind email-capture download forms.
  evidence:
  - status: 403
    url: https://acg-api.atombeamtech.com/openapi.json
  - status: 403
    url: https://acg-api.atombeamtech.com/
  - status: 302
    url: https://customersupport.atombeamtech.com/
  - status: 200
    url: https://www.atombeamtech.com/llms.txt
  - status: 404
    url: https://www.atombeamtech.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: 'AtomBeam Technologies is a Moraga, California software company founded in 2017 that sells "Compaction" — a machine-learning approach to shrinking machine-generated data that replaces recurring bit-level patterns with codewords drawn from a trained codebook, rather than compressing bytes. Its Neurpac product is an on-premises, protocol-agnostic bidirectional compaction tunnel that reduces IoT, telemetry and file payloads by roughly 75% while encrypting and obfuscating them in transit; Neurcom and PCM are earlier-stage research products. AtomBeam licenses the software to IoT device and gateway makers, satellite and LPWAN operators, telcos, and the US Department of Defense, and has raised capital through Regulation A and Regulation CF crowdfunding on StartEngine. There is no public developer API program: the customer-facing surface is the login-gated AtomBeam Customer Portal (codebook generation and simulation) plus a Jira Service Management support portal.'
image: https://cdn.prod.website-files.com/65ee960bca00890dd416e95c/65f8f36d0922a632a016240d_logo.png
layout: provider
modified: '2026-08-06'
name: AtomBeam
nav: Providers
network: true
random_paper: 47
slug: atombeam
tags:
- Company
- Data Compression
- Internet of Things
- Edge Computing
- Satellite Communications
- Machine Learning
- Data Management
- Defense
- Telemetry
---
