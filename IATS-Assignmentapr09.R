orderquantities = c(10000,15000,20000,25000,30000)
#Mean Computation
orderquantities_mean = mean(orderquantities)
print(paste("MEAN of Ordered Quantities <Mu>:" ,orderquantities_mean))

#Probability is given as 95% for the sales between 10K and 30K
zvalue = qnorm(1-(1-0.95)/2)
orderquantities_sd = round(10000/zvalue,2)
print(paste("STANDARD DEVIATION of Ordered Quantities <Sigma>:" ,orderquantities_sd))

#Plotting the Density
densityfuntion = dnorm(orderquantities,orderquantities_mean,orderquantities_sd)
plot(orderquantities, densityfuntion, col="red",xlab="", ylab="ProbabilityDensity", type = "b" , main="Normal Distribution",lwd=1)

#Computing the Probability of out of stock situation.
print( paste("Suggested Stock | Probability"))
xseq_suggestedstock = c(15000,18000,24000,28000)
for(suggestedstock in xseq_suggestedstock) {
if(suggestedstock < orderquantities_mean) {
  probability = round(pnorm(abs((suggestedstock-orderquantities_mean)/StandardDeviation)),2)
}
else {
  probability = round(1-pnorm((suggestedstock-orderquantities_mean)/StandardDeviation),2)
}
  print( paste(suggestedstock,"|", probability))
}

#Profit Calculation
InitialProfit = 24 - 16
LaterProfit = 5-16
WorstCaseStockSold = 10000
MostLikelyStockSold = 20000
BestCaseStockSold = 30000
print("SuggestedStock | WorstCaseStockSold -> TotalProfitInWorstCase | MostLikelyStockSold -> TotalProfitInMostLikelyCase | BestCaseStockSold -> TotalProfitInBestCase ")
xseq_orderedstock = c(15000,18000,24000,28000)
for(orderedstock in xseq_orderedstock) {
  if(orderedstock < WorstCaseStockSold) {
    TotalProfitInWorstCase = orderedstock * InitialProfit
  } else {
    TotalProfitInWorstCase = (WorstCaseStockSold * InitialProfit) + ((orderedstock-WorstCaseStockSold) * LaterProfit) 
  }
  
  if(orderedstock < MostLikelyStockSold) {
    TotalProfitInMostLikelyCase = orderedstock * InitialProfit
  } else {
    TotalProfitInMostLikelyCase = (MostLikelyStockSold * InitialProfit) + ((orderedstock-MostLikelyStockSold) * LaterProfit)
  }
   
  if(orderedstock < BestCaseStockSold) {
    TotalProfitInBestCase = orderedstock * InitialProfit
  } else {
    TotalProfitInBestCase = (BestCaseStockSold * InitialProfit) + ((orderedstock-BestCaseStockSold) * LaterProfit)
  }
  print( paste(orderedstock,"|",WorstCaseStockSold,"-> $",TotalProfitInWorstCase,"|",MostLikelyStockSold,"-> $",TotalProfitInMostLikelyCase,"|",BestCaseStockSold,"-> $",TotalProfitInBestCase))
}
