---
aid: merbridge
name: Merbridge
description: Merbridge is an open source, eBPF-based service mesh acceleration tool that replaces iptables rules with eBPF traffic interception and uses msg_redirect to shorten the datapath between sidecars and services. It is a CNCF Sandbox project and supports Istio, Linkerd2, and Kuma.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNCF
  - eBPF
  - Networking
  - Performance
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/merbridge/refs/heads/main/apis.yml
created: '2026-04-28'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: merbridge:merbridge
    name: Merbridge
    description: Merbridge uses eBPF to accelerate service mesh data planes by replacing iptables-based traffic interception and shortening the datapath between sidecars and services. It is a CNCF Sandbox project compatible with Istio, Linkerd2, and Kuma.
    humanURL: https://merbridge.io/
    tags:
      - eBPF
      - Service Mesh
    properties:
      - type: Documentation
        url: https://merbridge.io/docs/
      - type: Getting Started
        url: https://merbridge.io/docs/getting-started
      - type: Blog
        url: https://merbridge.io/blog/
      - type: SourceCode
        url: https://github.com/merbridge/merbridge
common:
  - type: Website
    url: https://merbridge.io/
  - type: Documentation
    url: https://merbridge.io/docs/
  - type: GitHub Organization
    url: https://github.com/merbridge
  - type: SourceCode
    url: https://github.com/merbridge/merbridge
  - type: Blog
    url: https://merbridge.io/blog/
  - type: Slack
    url: https://join.slack.com/t/merbridge/shared_invite/zt-11uc3z0w7-DMyv42eQ6s5YUxO5mZ5hwQ
  - type: Group
    url: https://groups.google.com/g/merbridge
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
