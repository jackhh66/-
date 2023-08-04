# -说明
  这里我会分享平时用python复现的指标代码，python辅助tv开发出来的策略相关功能，及交易所套利等源码
# -马丁_xrp 接入交易所 芝麻开门
  策略说明：
    1.添加布林带防止行情瞬间下跌仓位过重；
      这个策略是在tradingview优化过的马丁策略，实时计算15分钟的布林带，当行情下跌时，策略进行加仓，当最新价格超过布林带的下轨时，停止加仓，待价格回到下轨内时，且15分钟K柱收盘后再进行补仓。
    2.添加移动止盈止损功能；
      马丁将价格区分了若干个等份，而我们添加的这个功能，是将一个区间再次分成若干个区间。那么当行情上涨时，我们其中的一个加仓的仓位利润到达千4时，直接平仓，减仓后行情下跌时又将上一次仓位数加回来，
    这样子我们就可以把成本价拉低，以减少风险。
  优点：观察历史行情发现btc行情下跌15分钟内的波动有30%，所以我们在这种情况下如果让策略一直补仓，会面临爆仓的风险，添加布林带防止仓位过重，且可以保证行情下跌过快，在谷底加仓。
  缺点：利润会减少。
