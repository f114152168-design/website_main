# Render deployment instructions for website_main

## 部署到 Render 的步驟

### 1. 準備工作
- ✅ `Procfile` - 已建立
- ✅ `requirements.txt` - 已更新（包含 openai）
- ✅ `app.py` - Flask 應用入口
- ✅ `application/application.py` - 路由配置
- ✅ `application/ai_service.py` - AI 服務

### 2. 在 Render 上建立 Web Service
1. 登入 [render.com](https://render.com)
2. 點擊「+ New」→ 選擇「Web Service」
3. 連接你的 GitHub 儲存庫 `f114152168-design/website_main`
4. 填寫以下資訊：

**基本設定：**
- Name: `website-main` (或你喜歡的名稱)
- Environment: `Python 3`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Plan: 選擇適合的方案（免費方案 Free 可用）

### 3. 設定環境變數
在 Render 的 "Environment" 部分新增：

```
OPENAI_API_KEY=your_api_key_here
```

替換 `your_api_key_here` 為你的 OpenAI API 金鑰

### 4. 部署
1. 點擊「Create Web Service」
2. Render 會自動從 GitHub 拉取程式碼並部署
3. 部署完成後，你會得到一個 URL，例如：`https://website-main.onrender.com`

### 5. 訪問你的應用
- 首頁：`https://your-app.onrender.com/`
- AI 文字生成器：`https://your-app.onrender.com/ai-generator`

## 常見問題

### Q: 部署失敗怎麼辦？
A: 檢查 Render 的 Logs：
- 點擊 Web Service
- 查看「Logs」頁籤
- 檢查錯誤訊息

### Q: OpenAI API 金鑰在哪裡取得？
A: 
1. 訪問 [platform.openai.com](https://platform.openai.com)
2. 登入帳戶
3. 進入 API Keys
4. 建立新的 API Key
5. 複製 Key 到 Render 的環境變數

### Q: 如何更新應用？
A: 只需推送程式碼到 GitHub，Render 會自動偵測並重新部署

### Q: 應用休眠怎麼辦？
A: 免費方案會在 15 分鐘無活動後休眠。如需避免，升級到付費方案或使用 UptimeRobot 保活。

## 部署後的檢查清單

- [ ] 訪問主頁確認可正常載入
- [ ] 訪問 `/ai-generator` 頁面
- [ ] 測試 AI 文字生成功能
- [ ] 檢查所有路由是否正常
- [ ] 驗證 OpenAI API 連線
