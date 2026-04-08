---
aid: amazon-vpn
url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/apis.yml
apis:
- aid: amazon-vpn:aws-vpn-api
  name: AWS VPN API
  description: The AWS VPN API (part of the Amazon EC2 API) provides programmatic access to create and manage VPN connections, customer gateways, virtual private gateways, and Client VPN endpoints. It enables configuration of Site-to-Site VPN and Client VPN for secure hybrid connectivity.
  humanURL: https://aws.amazon.com/vpn/
  baseURL: https://ec2.amazonaws.com
  tags:
  - AWS
  - Networking
  - Security
  - VPN
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/vpn/latest/s2svpn/
  - type: Reference
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-vpn.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html
  - type: Pricing
    url: https://aws.amazon.com/vpn/pricing/
  - type: FAQ
    url: https://aws.amazon.com/vpn/faqs/
name: Amazon VPN
tags:
- AWS
- Networking
- Security
- VPN
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: 'AWS VPN solutions establish secure connections between on-premises networks, remote offices, client devices, and the AWS global network. AWS offers two types of private connectivity: AWS Site-to-Site VPN and AWS Client VPN, enabling encrypted tunnels between your network and Amazon Virtual Private Cloud.'
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

