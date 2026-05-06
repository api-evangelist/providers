---
aid: vpn
name: VPN
description: A VPN (Virtual Private Network) creates an encrypted tunnel between a user's device and a remote network, protecting data from interception and masking the user's IP address. VPN technology is widely used for secure remote access to corporate networks, protecting privacy on public Wi-Fi, and bypassing geographic content restrictions. This index documents VPN providers, protocols, and APIs relevant to the VPN technology landscape including NordVPN, OpenVPN, WireGuard, Tailscale, and cloud provider VPN services.
tags:
  - Encryption
  - Networking
  - Privacy
  - Security
  - VPN
type: Index
url: https://en.wikipedia.org/wiki/Virtual_private_network
apis:
  - aid: vpn:nordvpn-api
    name: NordVPN API
    tags:
      - Encryption
      - Networking
      - Privacy
      - Security
      - VPN
    humanURL: https://api.nordvpn.com/
    baseURL: https://api.nordvpn.com/v1
    description: NordVPN's public API provides server listings, recommendations, and user credential retrieval for programmatic VPN configuration, especially useful for WireGuard (NordLynx) configuration generation.
    properties:
      - url: https://api.nordvpn.com/v1/servers
        type: DataFeed
        description: NordVPN server list endpoint.
      - url: https://api.nordvpn.com/v1/servers/recommendations
        type: DataFeed
        description: NordVPN recommended server endpoint.
      - url: https://sleeplessbeastie.eu/2019/02/18/how-to-use-public-nordvpn-api/
        type: Documentation
        description: Community documentation for the NordVPN public API.
  - aid: vpn:tailscale-api
    name: Tailscale API
    tags:
      - Encryption
      - Mesh Network
      - Networking
      - Privacy
      - Security
      - VPN
      - WireGuard
      - Zero Trust
    humanURL: https://tailscale.com/api
    baseURL: https://api.tailscale.com/api/v2
    description: Tailscale provides a REST API for managing tailnets (private mesh networks), devices, users, access control lists, and network configuration. Built on WireGuard, Tailscale enables zero-configuration VPN for teams and organizations.
    properties:
      - url: https://tailscale.com/api
        type: Documentation
        description: Official Tailscale API documentation.
      - url: https://api.tailscale.com/api/v2
        type: BaseURL
        description: Tailscale API v2 base URL.
  - aid: vpn:aws-vpn
    name: AWS VPN API
    tags:
      - AWS
      - Cloud
      - Encryption
      - Networking
      - Security
      - VPN
    humanURL: https://docs.aws.amazon.com/vpn/
    baseURL: https://ec2.amazonaws.com/
    description: AWS Site-to-Site VPN and AWS Client VPN provide managed VPN solutions on AWS infrastructure. Managed via the AWS EC2 API and AWS CLI for creating virtual private gateways, customer gateways, and VPN connections.
    properties:
      - url: https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html
        type: Documentation
        description: AWS Site-to-Site VPN documentation.
      - url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/
        type: Documentation
        description: AWS Client VPN documentation.
  - aid: vpn:azure-vpn
    name: Azure VPN Gateway API
    tags:
      - Azure
      - Cloud
      - Encryption
      - Networking
      - Security
      - VPN
    humanURL: https://learn.microsoft.com/en-us/azure/vpn-gateway/
    baseURL: https://management.azure.com/
    description: Azure VPN Gateway provides managed site-to-site, point-to-site, and VNet-to-VNet VPN connections. Managed via Azure Resource Manager REST API and Azure CLI.
    properties:
      - url: https://learn.microsoft.com/en-us/azure/vpn-gateway/
        type: Documentation
        description: Azure VPN Gateway documentation.
      - url: https://learn.microsoft.com/en-us/rest/api/network/vpn-gateways
        type: Documentation
        description: Azure VPN Gateways REST API reference.
access: 3rd-Party
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
common:
  - url: https://en.wikipedia.org/wiki/Virtual_private_network
    name: VPN Wikipedia Article
    type: Reference
    description: Comprehensive reference on VPN technology and protocols.
  - url: https://www.wireguard.com/
    name: WireGuard Protocol
    type: Standard
    description: Modern, high-performance VPN protocol standard.
  - url: https://openvpn.net/
    name: OpenVPN
    type: Standard
    description: Open-source VPN protocol and software suite.
  - url: https://tailscale.com/
    name: Tailscale
    type: Portal
    description: WireGuard-based mesh VPN for teams with REST management API.
  - url: https://www.nordvpn.com/
    name: NordVPN
    type: Website
    description: Commercial VPN provider with public server API.
  - url: https://protonvpn.com/
    name: ProtonVPN
    type: Website
    description: Privacy-focused VPN provider by the Proton team.
  - url: https://github.com/qdm12/gluetun
    name: Gluetun
    type: OpenSource
    description: Docker VPN client supporting multiple providers via OpenVPN and WireGuard.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
