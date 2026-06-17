---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: '3ee404cc-5cce-4ea1-8c3d-802a025ae5e0'
  PropagateID: '3ee404cc-5cce-4ea1-8c3d-802a025ae5e0'
  ReservedCode1: '6620266e-a4fc-4c20-8ea6-89c2dd589184'
  ReservedCode2: '6620266e-a4fc-4c20-8ea6-89c2dd589184'
---

# AIGate Shell Website

AIGate 是一个企业级 AI 模型聚合网关的前端壳网站，基于 Vue3 + TailwindCSS v4 构建。

## 架构

AIGate 壳网站仅服务于落地页（`/`），所有其他路径（`/login`、`/register`、`/console` 等）代理至 new-api 后端，通过 Nginx `sub_filter` 进行品牌清洗，使终端用户看到 "AIGate" 而非 "New API"。

## 技术栈

- **前端**: Vue 3 + TailwindCSS v4 + Vite
- **反向代理**: Nginx（sub_filter 品牌清洗）
- **后端**: new-api（Calcium-Ion/new-api）
- **部署**: Docker + Nginx

## 本地开发

```bash
npm install
npm run dev
```

## 构建

```bash
npm run build
```

构建产物输出到 `dist/`，静态资源目录为 `aigate-assets/`（避免与 new-api 的 `/assets/` 冲突）。

## 部署

将构建产物部署到服务器 `/var/www/aigate/`，Nginx 配置见 `deploy/nginx/`。

## 端口说明

| 端口 | 用途 |
|------|------|
| 1002 | AIGate（公开访问，品牌清洗） |
| 1003 | new-api 原始界面（管理员直连） |

## 关键设计

1. **资源路径隔离**: AIGate 使用 `/aigate-assets/`，new-api 使用 `/assets/`，互不冲突
2. **品牌清洗**: Nginx sub_filter 将所有 "New API" / "new-api" / "newapi" 替换为 "AIGate"
3. **Header 翻译**: Nginx 将 `aigate-User` 转换为 `New-Api-User` 传递给上游
4. **注册关闭**: 通过数据库选项 `RegisterEnabled=false` 禁用公开注册