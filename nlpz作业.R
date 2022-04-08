## create by 姚岭君
#sessionInfo()
#R version 4.0.5 (2022-04-07)
#Platform: win11
#Running under: Windows 11

#setwd() #将工作目录设置为存有文本的目录
setwd('D:/r')
library(ggplot2)
library(wordcloud2)
filelist <- list.files(pattern=".*.txt")
filelist
m<-length(filelist)
entitylist <- lapply(filelist, function(x) read.csv(x,header = F,sep = "\t",col.names = c("pmid","start","end","name","type","ID")))
names(entitylist)<-c("cell_lines","chemical","disease","gene","mutation","species")
gene_table<-as.data.frame(table(entitylist[["gene"]]$ID)) 
View(gene_table)

mutation<-(entitylist[["mutation"]]) #找出突变内容
mutation <- mutation[!duplicated(mutation),]
mutation<-as.vector(mutation$name)
word_m<-table(mutation)
mu_order<-as.data.frame(word_m)#统计词频
wordcloud2(word_m,size=1)

gene<-(entitylist[["gene"]]) #找出基因
gene <- gene[!duplicated(gene),]#去重
name<-as.vector(gene$name)
word<-table(name)
gene_order<-as.data.frame(word)
wordcloud2(word,size = 2, fontWeight = "bold")
#disease
disease<-(entitylist[["disease"]]) #找出疾病
disease<-disease[!duplicated(disease),]
word_dis<-as.vector(disease$name)
word_dis<-table(word_dis)
dis_order<-as.data.frame(word_dis)
wordcloud2(dis_order,size = 1)
p<-ggplot(subset(gene_order,gene_order$Freq>30))+geom_bar(stat = "identity",fill="white",colour="dodgerblue")


##基因在染色体上分布情况柱状图
gene_result<-read.csv(file.choose(),header = T,sep = "\t") #导入gene_result文件
hg<-gene_result[gene_result$Org_name=="Homo sapiens",] #获取人类基因
chr<-as.data.frame(table(hg$chromosome)) #获取染色体出现频次
chr<-chr[-1,] #去除空的
#绘图
ggplot(data=chr,mapping=aes(x=Var1,y=Freq,fill=Var1,group=factor(1)))
+geom_bar(stat="identity")
+geom_text(aes(label = Freq, vjust = -0.8, hjust = 0.5, color = Var1))+xlab("Chromosome")+theme(legend.position = "none")