---
aid: amazon-vpn
name: Amazon VPN
description: 'AWS VPN solutions establish secure connections between on-premises networks, remote offices, client devices, and the AWS global network. AWS offers two types of private connectivity: AWS Site-to-Site VPN and AWS Client VPN, enabling encrypted tunnels between your network and Amazon Virtual Private Cloud.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Networking
  - Security
  - VPN
url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
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
      - type: APIReference
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-vpn.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html
      - type: Pricing
        url: https://aws.amazon.com/vpn/pricing/
      - type: FAQ
        url: https://aws.amazon.com/vpn/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/vpn/
  - type: Documentation
    url: https://docs.aws.amazon.com/vpn/latest/s2svpn/
  - type: Console
    url: https://console.aws.amazon.com/vpc/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/rules/amazon-vpn-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/vocabulary/amazon-vpn-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpn/refs/heads/main/capabilities/amazon-vpn-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon VPN.
      - name: API Access
        description: Programmatic access to Amazon VPN resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon VPN to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
