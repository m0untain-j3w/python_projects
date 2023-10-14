              #        Откроем необходимые библиотеки         #
library(ggplot2)


              #                Откроем датасет                #
data = read.csv("dataset/data.csv")


              #               Рассмотрим данные               #
str(data)
head(data, 3)


              #     Проверим датасет на наличие пропусков     #
sum(is.na(data))


              #        Рассмотрим отдельные параметры         #
summary(data)


              #  Избавимся от параметров, не имеющих значение #
              #   А именно континент, год и название страны   #
              #   (счастье населения явно от них не зависит)  #
data$continent = NULL
data$Year      = NULL
data$Country   = NULL


              #          Нормализуем все параметры            #
              #     Будем придерживаться диапазона [0, 1]     #
data$happiness_score   = data$happiness_score   / 10
data$cpi_score         = data$cpi_score         / 100
data$gdp_per_capita    = data$gdp_per_capita    / 10
data$family            = data$family            / 10
data$social_support    = data$social_support    / 10
data$dystopia_residual = data$dystopia_residual / 10
data = round(data, digits=2)


              #           Рассмотрим данные ещё раз           #
summary(data)


              #  Рассмотрим корреляции между уровнем счастья  #
              #              и другими параметрами            #
datacor = round(cor(data, data$happiness_score), digits = 2)
colnames(datacor) = c("happiness_score")
datacor


              #         Рассмотрим графики зависимости        #
ggplot(data, aes(happiness_score, params))+
  geom_point(aes(happiness_score, cpi_score,         col = "CPI"       ), alpha = 0.5)+
  geom_point(aes(happiness_score, gdp_per_capita,    col = "GDP"       ), alpha = 0.5)+
  geom_point(aes(happiness_score, freedom,           col = "FREEDOM"   ), alpha = 0.5)+
  geom_point(aes(happiness_score, health,            col = "HEALTH"    ), alpha = 0.5)+
  geom_point(aes(happiness_score, government_trust,  col = "GOV_TRUST" ), alpha = 0.5)+
  geom_point(aes(happiness_score, family,            col = "FAMILY"    ), alpha = 0.5)+
  geom_point(aes(happiness_score, generosity,        col = "GENEROSITY"), alpha = 0.5)+
  geom_point(aes(happiness_score, dystopia_residual, col = "DISTOPIA"  ), alpha = 0.5)+
  geom_point(aes(happiness_score, social_support,    col = "SUPPORT"   ), alpha = 0.5)

ggplot(data, aes(happiness_score, params))+
  geom_smooth(aes(happiness_score, cpi_score,         col = "CPI"       ), method = loess)+
  geom_smooth(aes(happiness_score, gdp_per_capita,    col = "GDP"       ), method = loess)+
  geom_smooth(aes(happiness_score, freedom,           col = "FREEDOM"   ), method = loess)+
  geom_smooth(aes(happiness_score, health,            col = "HEALTH"    ), method = loess)+
  geom_smooth(aes(happiness_score, government_trust,  col = "GOV_TRUST" ), method = loess)+
  geom_smooth(aes(happiness_score, family,            col = "FAMILY"    ), method = loess)+
  geom_smooth(aes(happiness_score, generosity,        col = "GENEROSITY"), method = loess)+
  geom_smooth(aes(happiness_score, dystopia_residual, col = "DISTOPIA"  ), method = loess)+
  geom_smooth(aes(happiness_score, social_support,    col = "SUPPORT"   ), method = loess)

ggplot(data, aes(happiness_score, params))+
  geom_smooth(aes(happiness_score, cpi_score,         col = "CPI"       ), method = lm)+
  geom_smooth(aes(happiness_score, gdp_per_capita,    col = "GDP"       ), method = lm)+
  geom_smooth(aes(happiness_score, freedom,           col = "FREEDOM"   ), method = lm)+
  geom_smooth(aes(happiness_score, health,            col = "HEALTH"    ), method = lm)+
  geom_smooth(aes(happiness_score, government_trust,  col = "GOV_TRUST" ), method = lm)+
  geom_smooth(aes(happiness_score, family,            col = "FAMILY"    ), method = lm)+
  geom_smooth(aes(happiness_score, generosity,        col = "GENEROSITY"), method = lm)+
  geom_smooth(aes(happiness_score, dystopia_residual, col = "DYSTOPIA"  ), method = lm)+
  geom_smooth(aes(happiness_score, social_support,    col = "SUPPORT"   ), method = lm)


              #           Разделим данные на обучающий        #
              #                и тестовый наборы              #
set.seed(1)
sample = sample(c(TRUE, FALSE), nrow(data), replace = TRUE, prob = c(0.7, 0.3))
data_train = data[sample, ]
data_test = data[!sample, ]


              #       Создадим модель линейной регрессии      #
model1 = lm(happiness_score ~ gdp_per_capita + health + freedom +
           dystopia_residual + government_trust + social_support +
           cpi_score + generosity, data_train)
summary(model1)
              # Наблюдаем, что "cpi_score и government_trust" #
              #       хуже всех предсказывают результат;      #
              #              Попробуем их убрать              #
model2 = lm(happiness_score ~ gdp_per_capita + health + freedom +
            dystopia_residual + social_support + generosity, data_train)
summary(model2)


              #        Рассмотрим предсказания моделей        #
test_predicted_values1 = round(data.frame(hs = data_test$happiness_score,  predicted = predict(model1, data_test[2:10])),  digits = 2)
test_predicted_values2 = round(data.frame(hs = data_test$happiness_score,  predicted = predict(model2, data_test[2:10])),  digits = 2)
              #     Для наглядности, сравним суммы ошибок     #
n1 = sum(abs(test_predicted_values1[ , 1] - test_predicted_values1[ , 2]))
n2 = sum(abs(test_predicted_values2[ , 1] - test_predicted_values2[ , 2]))

