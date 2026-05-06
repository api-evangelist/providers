---
aid: tcp-ip
name: TCP/IP
description: TCP/IP (Transmission Control Protocol/Internet Protocol) is the foundational communication protocol suite that powers the internet and most computer networks. It provides reliable, ordered delivery of data between applications across diverse network hardware through a layered architecture of protocols. The suite encompasses protocols at multiple layers including TCP, IP, UDP, HTTP, and many others, defined through IETF RFCs maintained at the RFC Editor.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Networking
  - Protocol
  - Internet
  - Standards
  - IETF
  - RFC
  - TCP
  - IP
created: '2025-01-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tcp-ip/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tcp-ip:sockets-api
    name: Berkeley Sockets API
    description: The de facto standard programming interface for TCP/IP networking, defined in RFC 3493. Implemented nearly ubiquitously in modern operating systems and programming languages, the Sockets API provides functions for creating network connections, sending and receiving data, and managing socket state.
    humanURL: https://www.rfc-editor.org/rfc/rfc3493
    tags:
      - Sockets
      - POSIX
      - Network Programming
      - RFC 3493
    properties:
      - type: Documentation
        url: https://www.rfc-editor.org/rfc/rfc3493
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc3493
common:
  - type: Documentation
    name: RFC Editor
    description: Official IETF RFC Editor with all TCP/IP protocol specifications.
    url: https://www.rfc-editor.org/
  - type: Documentation
    name: IETF Datatracker
    description: IETF document tracking and standards development.
    url: https://datatracker.ietf.org/
  - type: Specification
    name: RFC 9293 - TCP Specification
    description: The current canonical TCP specification, consolidating four decades of updates. Obsoletes RFC 793.
    url: https://www.rfc-editor.org/rfc/rfc9293
  - type: Specification
    name: RFC 791 - Internet Protocol
    description: The foundational Internet Protocol (IP) specification.
    url: https://www.rfc-editor.org/rfc/rfc791
  - type: Specification
    name: RFC 768 - UDP
    description: User Datagram Protocol specification.
    url: https://www.rfc-editor.org/rfc/rfc768
  - type: Specification
    name: RFC 1180 - TCP/IP Tutorial
    description: Educational overview of the TCP/IP protocol suite.
    url: https://www.rfc-editor.org/rfc/rfc1180
  - type: Specification
    name: RFC 3493 - Sockets API
    description: Basic Socket Interface Extensions for IPv6, the standard sockets programming API.
    url: https://www.rfc-editor.org/rfc/rfc3493
  - type: Specification
    name: RFC 4614 - TCP Roadmap
    description: A roadmap for Transmission Control Protocol (TCP) specification documents.
    url: https://www.rfc-editor.org/rfc/rfc4614
  - type: Website
    name: IETF Official Site
    url: https://www.ietf.org/
features:
  - name: Reliable Delivery
    description: TCP guarantees ordered, reliable delivery of data between endpoints.
  - name: Connection-Oriented Communication
    description: TCP establishes a connection via three-way handshake before data transfer.
  - name: Flow Control
    description: TCP window-based flow control prevents overwhelming receivers.
  - name: Congestion Control
    description: TCP algorithms (Reno, CUBIC, BBR) manage network congestion.
  - name: IPv4 and IPv6 Support
    description: Protocol suite supports both IPv4 (RFC 791) and IPv6 (RFC 2460) addressing.
  - name: Connectionless UDP
    description: UDP provides low-latency connectionless transport where reliability is handled at application layer.
  - name: Multiplexing via Ports
    description: Port numbers allow multiple services to share an IP address.
useCases:
  - name: Web Applications
    description: HTTP/HTTPS runs over TCP/IP for all web browser and server communication.
  - name: File Transfer
    description: FTP, SFTP, and SCP use TCP/IP for reliable file transfer.
  - name: Email
    description: SMTP, IMAP, and POP3 protocols use TCP/IP for email transmission.
  - name: Real-Time Communications
    description: WebRTC and VoIP use UDP over IP for low-latency media streams.
  - name: Network Programming
    description: Berkeley Sockets API provides the standard interface for TCP/IP network programming.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
