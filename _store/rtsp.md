---
aid: rtsp
name: RTSP
description: Real-Time Streaming Protocol (RTSP) is an application-level network protocol designed for controlling streaming media servers. Defined by IETF RFC 2326 (RTSP 1.0) and RFC 7826 (RTSP 2.0), it acts as a network remote control for multimedia servers, enabling on-demand delivery of real-time audio and video data. RTSP controls sessions between endpoints but relies on RTP (Real-time Transport Protocol) for actual media transport. It is widely used in IP cameras, DVR systems, media servers, and live streaming platforms.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Streaming
  - Video
  - Media
  - Protocol
  - Real-Time
created: '2025-01-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/rtsp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: rtsp:rtsp-protocol
    name: RTSP Protocol
    description: The Real-Time Streaming Protocol (RTSP) is a stateful protocol defined in RFC 2326 (1.0) and RFC 7826 (2.0). It defines methods including OPTIONS, DESCRIBE, SETUP, PLAY, PAUSE, RECORD, ANNOUNCE, GET_PARAMETER, SET_PARAMETER, and TEARDOWN for controlling streaming media sessions. RTSP URLs follow the rtsp:// scheme. Sessions are established before streaming begins and media is transmitted via RTP/RTCP on separate channels.
    humanURL: https://datatracker.ietf.org/doc/html/rfc7826
    baseURL: rtsp://
    tags:
      - Streaming
      - Video
      - Media
      - Protocol
      - IETF
      - RFC
    properties:
      - type: Documentation
        url: https://datatracker.ietf.org/doc/html/rfc7826
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc2326
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc7826
  - aid: rtsp:rtsp-implementations
    name: RTSP Implementations
    description: Common open-source RTSP server and client implementations used in production. MediaMTX (formerly rtsp-simple-server) is a ready-to-use media server supporting RTSP/RTMP/WebRTC with an HTTP API for management. GStreamer and FFmpeg provide RTSP client/server libraries. IP camera manufacturers (Axis, Hikvision, Dahua) expose RTSP streams at standard paths like rtsp://{host}:554/live or rtsp://{host}/stream.
    humanURL: https://github.com/bluenviron/mediamtx
    tags:
      - Streaming
      - Video
      - IP Camera
      - Open Source
      - MediaMTX
    properties:
      - type: Documentation
        url: https://github.com/bluenviron/mediamtx
common:
  - type: Specification
    url: https://datatracker.ietf.org/doc/html/rfc7826
  - type: Specification
    url: https://datatracker.ietf.org/doc/html/rfc2326
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Real-Time_Streaming_Protocol
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
