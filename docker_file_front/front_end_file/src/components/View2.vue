<template>
    <div class="title">
      <h3> Scenario 2 - Tweets by cities and genres </h3>
    </div>
    <div class="c1">
      <div ref="chart1" style="height: 400px;"></div>
      <ul>{{string}}</ul>
    </div>
    <div class="c23">
      <div class="c2" ref="chart2"></div>
      <div class="c3" ref="chart3"></div>
    </div>
    <div class="sub1">
      <ul>{{string2}}</ul>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            string: '# of tweets by cities',
            string2: 'sports genre and events',
            chart1: null,
            chart2: null,
            chart3: null,
            chart1Data: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://172.26.135.65:5000/view2');
                console.log(response.data);
                this.chart1Data = response.data;
                this.updateChart1();
                this.updateChart2();
                this.updateChart3();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart1() {
            this.chart1.setOption(
                {
                  tooltip: {
                    trigger: 'item'
                  },
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  series: [
                    {
                      name: 'Access From',
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: 25,
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      data: this.chart1Data[0]
                    }
                  ]
                }
            );
        },
        updateChart2() {
          this.chart2.setOption(
                {
                  legend: {},
                  tooltip: {},
                  dataset: {
                    source: this.chart1Data[1]
                  },
                  title: [
                    {
                      subtext: 'Sydney',
                      left: '25%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: 'Melbourne',
                      left: '75%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: 'Brisbane',
                      left: '25%',
                      top: '90%',
                      textAlign: 'center'
                    }
                  ],
                  series: [
                    {
                      type: 'pie',
                      radius: '20%',
                      center: ['25%', '30%']
                      // No encode specified, by default, it is '2012'.
                    },
                    {
                      type: 'pie',
                      radius: '20%',
                      center: ['75%', '30%'],
                      encode: {
                        itemName: '',
                        value: '2gmel'
                      }
                    },
                    {
                      type: 'pie',
                      radius: '20%',
                      center: ['25%', '75%'],
                      encode: {
                        itemName: '',
                        value: '3gbri'
                      }
                    }
                  ]
                }            
          )
        },
        updateChart3() {
          this.chart3.setOption(
              {
                title: {
                },
                tooltip: {
                  trigger: 'item'
                },
                legend: {
                  orient: 'vertical',
                  left: 'left'
                },
                series: [
                  {
                    name: 'Access From',
                    type: 'pie',
                    radius: '50%',
                    data: this.chart1Data[2],
                    emphasis: {
                      itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                      }
                    }
                  }
                ]
              }            
          )
        }
    },
    mounted() {
        this.chart1 = echarts.init(this.$refs.chart1);
        this.chart2 = echarts.init(this.$refs.chart2);
        this.chart3 = echarts.init(this.$refs.chart3);
        this.getData1();
    },
}
</script>

<style lang="scss" scoped>
.title {
  margin-top: 40px;
}
.c23 {
  display: flex;
  height: 400px;
  margin-left: 50px;
  .c2 {
    display: flex;
    height: 500px;
    width: 600px;
    margin-left: 50px;
  }
  .c3 {
    display: flex;
    height: 500px;
    width: 600px;
    margin-left: 50px;
  }
}
.sub1 {
  margin-top: 80px;
}
</style>
