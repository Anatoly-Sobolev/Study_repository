<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  
  <xsl:template match="/">
    <html lang="ru">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>Знаменитые омичи</title>
        <style>
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          }
          
          body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #333;
            line-height: 1.6;
            padding: 20px;
            min-height: 100vh;
          }
          
          .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
          }
          
          header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(90deg, #2c3e50, #4a6491);
            color: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
          }
          
          h1 {
            font-size: 2.8rem;
            margin-bottom: 10px;
            letter-spacing: 1px;
          }
          
          .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            font-weight: 300;
          }
          
          .region-section {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease;
          }
          
          .region-section:hover {
            transform: translateY(-5px);
          }
          
          .region-title {
            color: #2c3e50;
            font-size: 2rem;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #3498db;
            display: inline-block;
          }
          
          .group-section {
            margin-bottom: 25px;
          }
          
          .group-title {
            color: #2980b9;
            font-size: 1.5rem;
            margin: 20px 0 15px;
            padding-left: 15px;
            border-left: 4px solid #3498db;
          }
          
          .person-list {
            list-style: none;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
            gap: 25px;
          }
          
          .person-card {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 20px;
            border-left: 5px solid #3498db;
            transition: all 0.3s ease;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
            display: flex;
            flex-direction: column;
          }
          
          .person-card:hover {
            background: #eef5ff;
            box-shadow: 0 5px 15px rgba(52, 152, 219, 0.2);
          }
          
          .person-header {
            display: flex;
            gap: 20px;
            margin-bottom: 15px;
          }
          
          .person-image {
            width: 120px;
            height: 120px;
            border-radius: 8px;
            object-fit: cover;
            border: 3px solid #3498db;
            background: #e0e0e0;
            flex-shrink: 0;
          }
          
          .image-placeholder {
            width: 120px;
            height: 120px;
            border-radius: 8px;
            border: 3px solid #3498db;
            background: linear-gradient(135deg, #e0e0e0, #b0b0b0);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #777;
            font-size: 0.9rem;
            text-align: center;
            padding: 10px;
            flex-shrink: 0;
          }
          
          .person-name-container {
            flex: 1;
          }
          
          .person-name {
            color: #2c3e50;
            font-size: 1.5rem;
            margin-bottom: 8px;
          }
          
          .person-id {
            background: #3498db;
            color: white;
            font-size: 0.8rem;
            padding: 3px 10px;
            border-radius: 20px;
            font-weight: 500;
            display: inline-block;
          }
          
          .person-info {
            margin-top: 10px;
          }
          
          .info-row {
            margin-bottom: 8px;
            display: flex;
            align-items: flex-start;
          }
          
          .label {
            font-weight: 600;
            color: #3498db;
            min-width: 140px;
            font-size: 0.95rem;
          }
          
          .value {
            color: #555;
            flex: 1;
            font-size: 0.95rem;
          }
          
          .years {
            color: #e74c3c;
            font-weight: 500;
          }
          
          footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            color: #7f8c8d;
            font-size: 0.9rem;
            border-top: 1px solid #eee;
          }
          
          @media (max-width: 768px) {
            .person-list {
              grid-template-columns: 1fr;
            }
            
            .person-header {
              flex-direction: column;
              align-items: center;
              text-align: center;
            }
            
            .person-image, .image-placeholder {
              width: 150px;
              height: 150px;
            }
            
            h1 {
              font-size: 2.2rem;
            }
            
            .container {
              padding: 10px;
            }
          }
        </style>
      </head>
      <body>
        <div class="container">
          <header>
            <h1>Знаменитые омичи</h1>
            <div class="subtitle">Коллекция выдающихся людей Омска и Омской области</div>
          </header>
          
          <main>
            <xsl:for-each select="omichs/collection/region">
              <section class="region-section">
                <h2 class="region-title">
                  <xsl:value-of select="@type"/>
                </h2>
                
                <xsl:for-each select="group">
                  <div class="group-section">
                    <h3 class="group-title">
                      <xsl:value-of select="@name"/>
                    </h3>
                    
                    <ul class="person-list">
                      <xsl:for-each select="person">
                        <li class="person-card">
                          <div class="person-header">
                            <xsl:choose>
                              <xsl:when test="picture != ''">
                                <img class="person-image" src="{picture}" alt="{name}" 
                                     onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"/>
                                <div class="image-placeholder" style="display:none;">
                                  Фото не найдено<br/>
                                  <xsl:value-of select="substring(name, 1, 1)"/>
                                  <xsl:value-of select="substring(name, string-length(name) - 3, 4)"/>
                                </div>
                              </xsl:when>
                              <xsl:otherwise>
                                <div class="image-placeholder">
                                  Нет фото<br/>
                                  <xsl:value-of select="substring(name, 1, 1)"/>
                                  <xsl:value-of select="substring(name, string-length(name) - 3, 4)"/>
                                </div>
                              </xsl:otherwise>
                            </xsl:choose>
                            <div class="person-name-container">
                              <div class="person-name">
                                <xsl:value-of select="name"/>
                              </div>
                              <span class="person-id">ID: <xsl:value-of select="@id"/></span>
                            </div>
                          </div>
                          
                          <div class="person-info">
                            <div class="info-row">
                              <span class="label">Годы жизни:</span>
                              <span class="value years">
                                <xsl:value-of select="lifespan/born"/>
                                <xsl:if test="lifespan/died">
                                  — <xsl:value-of select="lifespan/died"/>
                                </xsl:if>
                              </span>
                            </div>
                            
                            <div class="info-row">
                              <span class="label">Краткая биография:</span>
                              <span class="value"><xsl:value-of select="bio"/></span>
                            </div>
                            
                            <div class="info-row">
                              <span class="label">Деятельность:</span>
                              <span class="value"><xsl:value-of select="work"/></span>
                            </div>
                          </div>
                        </li>
                      </xsl:for-each>
                    </ul>
                  </div>
                </xsl:for-each>
              </section>
            </xsl:for-each>
          </main>
          
          <footer>
            <p>© Коллекция известных омичей. Данные представлены в ознакомительных целях.</p>
          </footer>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>